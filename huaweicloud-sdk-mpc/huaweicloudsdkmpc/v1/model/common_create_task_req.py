# coding: utf-8

import pprint
import re

import six





class CommonCreateTaskReq:


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
        'sync': 'int'
    }

    attribute_map = {
        'input': 'input',
        'output': 'output',
        'user_data': 'user_data',
        'sync': 'sync'
    }

    def __init__(self, input=None, output=None, user_data=None, sync=0):
        """CommonCreateTaskReq - a model defined in huaweicloud sdk"""
        
        

        self._input = None
        self._output = None
        self._user_data = None
        self._sync = None
        self.discriminator = None

        if input is not None:
            self.input = input
        if output is not None:
            self.output = output
        if user_data is not None:
            self.user_data = user_data
        if sync is not None:
            self.sync = sync

    @property
    def input(self):
        """Gets the input of this CommonCreateTaskReq.


        :return: The input of this CommonCreateTaskReq.
        :rtype: ObsObjInfo
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this CommonCreateTaskReq.


        :param input: The input of this CommonCreateTaskReq.
        :type: ObsObjInfo
        """
        self._input = input

    @property
    def output(self):
        """Gets the output of this CommonCreateTaskReq.


        :return: The output of this CommonCreateTaskReq.
        :rtype: ObsObjInfo
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this CommonCreateTaskReq.


        :param output: The output of this CommonCreateTaskReq.
        :type: ObsObjInfo
        """
        self._output = output

    @property
    def user_data(self):
        """Gets the user_data of this CommonCreateTaskReq.

        用户自定义数据。 

        :return: The user_data of this CommonCreateTaskReq.
        :rtype: str
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        """Sets the user_data of this CommonCreateTaskReq.

        用户自定义数据。 

        :param user_data: The user_data of this CommonCreateTaskReq.
        :type: str
        """
        self._user_data = user_data

    @property
    def sync(self):
        """Gets the sync of this CommonCreateTaskReq.

        是否同步处理, - 0：排队处理 - 1：同步处理  默认值：0 

        :return: The sync of this CommonCreateTaskReq.
        :rtype: int
        """
        return self._sync

    @sync.setter
    def sync(self, sync):
        """Sets the sync of this CommonCreateTaskReq.

        是否同步处理, - 0：排队处理 - 1：同步处理  默认值：0 

        :param sync: The sync of this CommonCreateTaskReq.
        :type: int
        """
        self._sync = sync

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
        if not isinstance(other, CommonCreateTaskReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
