class Promise:
    def __init__(self, executor):
        """
        Initializes a Promise instance.

        Args:
            executor (callable): A function that takes two parameters, resolve and reject.
                - resolve: A function to call when the asynchronous operation is successful.
                - reject: A function to call when there is an error.
        """
        self.state = 'pending'
        self.result = None
        self.error = None
        self.on_fulfilled = []
        self.on_rejected = []

        def resolve(value):
            """
            Resolve the Promise with a given value.

            Args:
                value: The value to fulfill the Promise with.
            """
            if self.state == 'pending':
                self.state = 'fulfilled'
                self.result = value
                for callback in self.on_fulfilled:
                    callback(value)

        def reject(error):
            """
            Reject the Promise with a given error.

            Args:
                error: The error to reject the Promise with.
            """
            if self.state == 'pending':
                self.state = 'rejected'
                self.error = error
                for callback in self.on_rejected:
                    callback(error)

        try:
            executor(resolve, reject)
        except Exception as e:
            reject(e)

    def then(self, on_fulfilled, on_rejected=None):
        """
        Attach callbacks to be executed when the Promise is resolved or rejected.

        Args:
            on_fulfilled (callable): A function to be called when the Promise is fulfilled.
            on_rejected (callable, optional): A function to be called when the Promise is rejected.

        Returns:
            Promise: A new Promise that is resolved with the result of the called callback.
        """
        def handle_fulfilled(result):
            try:
                if on_fulfilled:
                    new_result = on_fulfilled(result)
                    if isinstance(new_result, Promise):
                        new_result.then(self.resolve, self.reject)
                    else:
                        self.resolve(new_result)
                else:
                    self.resolve(result)
            except Exception as e:
                self.reject(e)

        def handle_rejected(error):
            if on_rejected:
                try:
                    new_error = on_rejected(error)
                    if isinstance(new_error, Promise):
                        new_error.then(self.resolve, self.reject)
                    else:
                        self.reject(new_error)
                except Exception as e:
                    self.reject(e)
            else:
                self.reject(error)

        if self.state == 'fulfilled':
            handle_fulfilled(self.result)
        elif self.state == 'rejected':
            handle_rejected(self.error)
        else:
            self.on_fulfilled.append(handle_fulfilled)
            if on_rejected:
                self.on_rejected.append(handle_rejected)

        return self

    def catch(self, on_rejected):
        """
        Attach a callback to be executed when the Promise is rejected.

        Args:
            on_rejected (callable): A function to be called when the Promise is rejected.

        Returns:
            Promise: A new Promise that is resolved with the result of the called callback.
        """
        return self.then(None, on_rejected)

    def resolve(self, value):
        """
        Resolve the Promise with a given value.

        Args:
            value: The value to fulfill the Promise with.
        """
        if self.state == 'pending':
            self.state = 'fulfilled'
            self.result = value
            for callback in self.on_fulfilled:
                callback(value)

    def reject(self, error):
        """
        Reject the Promise with a given error.

        Args:
            error: The error to reject the Promise with.
        """
        if self.state == 'pending':
            self.state = 'rejected'
            self.error = error
            for callback in self.on_rejected:
                callback(error)
