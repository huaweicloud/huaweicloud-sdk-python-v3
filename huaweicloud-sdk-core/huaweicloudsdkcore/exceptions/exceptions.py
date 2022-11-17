# coding: utf-8
"""
 Licensed to the Apache Software Foundation (ASF) under one
 or more contributor license agreements.  See the NOTICE file
 distributed with this work for additional information
 regarding copyright ownership.  The ASF licenses this file
 to you under the Apache LICENSE, Version 2.0 (the
 "LICENSE"); you may not use this file except in compliance
 with the LICENSE.  You may obtain a copy of the LICENSE at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing,
 software distributed under the LICENSE is distributed on an
 "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 KIND, either express or implied.  See the LICENSE for the
 specific language governing permissions and limitations
 under the LICENSE.
"""

import six


class SdkException(Exception):
    def __init__(self):
        """
        The base exception class.
        """
        pass


class ConnectionException(SdkException):
    def __init__(self, err_message):
        """
        The base exception class of connection exceptions.
        """
        super(ConnectionException, self).__init__()
        self.err_message = err_message

    def __str__(self):
        return "ConnectionException - %s" % self.err_message


class HostUnreachableException(ConnectionException):
    def __init__(self, err_message):
        """
        Host Unreachable Exception
        """
        super(HostUnreachableException, self).__init__(err_message)
        self.err_message = err_message

    def __str__(self):
        return "HostUnreachableException - %s" % self.err_message


class SslHandShakeException(ConnectionException):
    def __init__(self, err_message):
        """
        Ssl HandShake Exception
        """
        super(SslHandShakeException, self).__init__(err_message)
        self.err_message = err_message

    def __str__(self):
        return "SslHandShakeException - %s" % self.err_message


def render_path(path_to_item):
    """Returns a string representation of a path"""
    result = ""
    for pth in path_to_item:
        if isinstance(pth, six.integer_types):
            result += "[{0}]".format(pth)
        else:
            result += "['{0}']".format(pth)
    return result


class ApiTypeError(TypeError):
    def __init__(self, msg, path_to_item=None, valid_classes=None,
                 key_type=None):
        """ Raises an exception for TypeErrors

        Args:
            msg (str): the exception message

        Keyword Args:
            path_to_item (list): a list of keys an indices to get to the
                                 current_item
                                 None if unset
            valid_classes (tuple): the primitive classes that current item
                                   should be an instance of
                                   None if unset
            key_type (bool): False if our value is a value in a dict
                             True if it is a key in a dict
                             False if our item is an item in a list
                             None if unset
        """
        self.path_to_item = path_to_item
        self.valid_classes = valid_classes
        self.key_type = key_type
        full_msg = msg
        if path_to_item:
            full_msg = "%s at %s" % (msg, render_path(path_to_item))
        super(ApiTypeError, self).__init__(full_msg)


class ApiValueError(ValueError):
    def __init__(self, msg, path_to_item=None):
        """
        Args:
            msg (str): the exception message

        Keyword Args:
            path_to_item (list) the path to the exception in the
                received_data dict. None if unset
        """

        self.path_to_item = path_to_item
        full_msg = msg
        if path_to_item:
            full_msg = "%s at %s" % (msg, render_path(path_to_item))
        super(ApiValueError, self).__init__(full_msg)


class ApiKeyError(KeyError):
    def __init__(self, msg, path_to_item=None):
        """
        Args:
            msg (str): the exception message

        Keyword Args:
            path_to_item (None/list) the path to the exception in the
                received_data dict
        """
        self.path_to_item = path_to_item
        full_msg = msg
        if path_to_item:
            full_msg = "%s at %s" % (msg, render_path(path_to_item))
        super(ApiKeyError, self).__init__(full_msg)


class ServiceResponseException(SdkException):
    def __init__(self, status_code, sdk_error):
        """
        The base exception class of service response exceptions.
        """
        self.status_code = status_code
        self.error_msg = sdk_error.error_msg
        self.error_code = sdk_error.error_code
        self.request_id = sdk_error.request_id

    def __str__(self):
        return "ServiceResponseException - {status_code:%s,request_id:%s,error_code:%s,error_msg:%s }" % (
            self.status_code, self.request_id, self.error_code, self.error_msg)


class ClientRequestException(ServiceResponseException):
    def __init__(self, status_code, sdk_error):
        """
        Client Request Exception
        """
        super(ClientRequestException, self).__init__(status_code, sdk_error)
        self.status_code = status_code
        self.error_msg = sdk_error.error_msg
        self.error_code = sdk_error.error_code
        self.request_id = sdk_error.request_id

    def __str__(self):
        return "ClientRequestException - {status_code:%s,request_id:%s,error_code:%s,error_msg:%s }" % (
            self.status_code, self.request_id, self.error_code, self.error_msg)


class ServerResponseException(ServiceResponseException):
    def __init__(self, status_code, sdk_error):
        """
        Server Response Exception
        """
        super(ServerResponseException, self).__init__(status_code, sdk_error)
        self.status_code = status_code
        self.error_msg = sdk_error.error_msg
        self.error_code = sdk_error.error_code
        self.request_id = sdk_error.request_id

    def __str__(self):
        return "ServerResponseException - {status_code:%s,request_id:%s,error_code:%s,error_msg:%s }" % (
            self.status_code, self.request_id, self.error_code, self.error_msg)


class RequestTimeoutException(SdkException):
    def __init__(self, err_message):
        """
        The base exception class of timeout exceptions.
        """
        super(self)
        self.err_message = err_message

    def __str__(self):
        return "RequestTimeoutException - %s" % self.err_message


class CallTimeoutException(RequestTimeoutException):
    def __init__(self, err_message):
        """
        Call Timeout Exception
        """
        super(CallTimeoutException, self).__init__(err_message)
        self.err_message = err_message

    def __str__(self):
        return "CallTimeoutException - %s" % self.err_message


class RetryOutageException(RequestTimeoutException):
    def __init__(self, err_message):
        """
        Retry Outage Exception
        """
        super(RetryOutageException, self).__init__(err_message)
        self.err_message = err_message

    def __str__(self):
        return "RetryOutageException - %s" % self.err_message


class SdkError(object):
    def __init__(self, request_id=None, error_code=None, error_msg=None):
        self.error_msg = error_msg
        self.error_code = error_code
        self.request_id = request_id
