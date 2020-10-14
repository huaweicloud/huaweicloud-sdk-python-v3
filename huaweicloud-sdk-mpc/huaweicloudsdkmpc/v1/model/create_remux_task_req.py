# coding: utf-8

import pprint
import re

import six





class CreateRemuxTaskReq:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'input': 'ObsObjInfo',
        'output': 'ObsObjInfo',
        'user_data': 'str',
        'sync': 'int',
        'output_param': 'RemuxOutputParam',
        'notify_url': 'str'
    }

    attribute_map = {
        'input': 'input',
        'output': 'output',
        'user_data': 'user_data',
        'sync': 'sync',
        'output_param': 'output_param',
        'notify_url': 'notify_url'
    }

    def __init__(self, input=None, output=None, user_data=None, sync=0, output_param=None, notify_url=None):
        """CreateRemuxTaskReq - a model defined in huaweicloud sdk"""
        
        

        self._input = None
        self._output = None
        self._user_data = None
        self._sync = None
        self._output_param = None
        self._notify_url = None
        self.discriminator = None

        if input is not None:
            self.input = input
        if output is not None:
            self.output = output
        if user_data is not None:
            self.user_data = user_data
        if sync is not None:
            self.sync = sync
        if output_param is not None:
            self.output_param = output_param
        if notify_url is not None:
            self.notify_url = notify_url

    @property
    def input(self):
        """Gets the input of this CreateRemuxTaskReq.


        :return: The input of this CreateRemuxTaskReq.
        :rtype: ObsObjInfo
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this CreateRemuxTaskReq.


        :param input: The input of this CreateRemuxTaskReq.
        :type: ObsObjInfo
        """
        self._input = input

    @property
    def output(self):
        """Gets the output of this CreateRemuxTaskReq.


        :return: The output of this CreateRemuxTaskReq.
        :rtype: ObsObjInfo
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this CreateRemuxTaskReq.


        :param output: The output of this CreateRemuxTaskReq.
        :type: ObsObjInfo
        """
        self._output = output

    @property
    def user_data(self):
        """Gets the user_data of this CreateRemuxTaskReq.

        用户自定义数据。 

        :return: The user_data of this CreateRemuxTaskReq.
        :rtype: str
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        """Sets the user_data of this CreateRemuxTaskReq.

        用户自定义数据。 

        :param user_data: The user_data of this CreateRemuxTaskReq.
        :type: str
        """
        self._user_data = user_data

    @property
    def sync(self):
        """Gets the sync of this CreateRemuxTaskReq.

        是否同步处理, - 0：排队处理 - 1：同步处理  默认值：0 

        :return: The sync of this CreateRemuxTaskReq.
        :rtype: int
        """
        return self._sync

    @sync.setter
    def sync(self, sync):
        """Sets the sync of this CreateRemuxTaskReq.

        是否同步处理, - 0：排队处理 - 1：同步处理  默认值：0 

        :param sync: The sync of this CreateRemuxTaskReq.
        :type: int
        """
        self._sync = sync

    @property
    def output_param(self):
        """Gets the output_param of this CreateRemuxTaskReq.


        :return: The output_param of this CreateRemuxTaskReq.
        :rtype: RemuxOutputParam
        """
        return self._output_param

    @output_param.setter
    def output_param(self, output_param):
        """Sets the output_param of this CreateRemuxTaskReq.


        :param output_param: The output_param of this CreateRemuxTaskReq.
        :type: RemuxOutputParam
        """
        self._output_param = output_param

    @property
    def notify_url(self):
        """Gets the notify_url of this CreateRemuxTaskReq.

        提供给mpe通知回调用的的url 

        :return: The notify_url of this CreateRemuxTaskReq.
        :rtype: str
        """
        return self._notify_url

    @notify_url.setter
    def notify_url(self, notify_url):
        """Sets the notify_url of this CreateRemuxTaskReq.

        提供给mpe通知回调用的的url 

        :param notify_url: The notify_url of this CreateRemuxTaskReq.
        :type: str
        """
        self._notify_url = notify_url

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateRemuxTaskReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
