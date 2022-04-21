# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        'user_data': 'str'
    }

    attribute_map = {
        'input': 'input',
        'output': 'output',
        'user_data': 'user_data'
    }

    def __init__(self, input=None, output=None, user_data=None):
        """CommonCreateTaskReq

        The model defined in huaweicloud sdk

        :param input: 
        :type input: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        :param output: 
        :type output: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        :param user_data: 用户自定义数据。 
        :type user_data: str
        """
        
        

        self._input = None
        self._output = None
        self._user_data = None
        self.discriminator = None

        if input is not None:
            self.input = input
        if output is not None:
            self.output = output
        if user_data is not None:
            self.user_data = user_data

    @property
    def input(self):
        """Gets the input of this CommonCreateTaskReq.


        :return: The input of this CommonCreateTaskReq.
        :rtype: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this CommonCreateTaskReq.


        :param input: The input of this CommonCreateTaskReq.
        :type input: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        """
        self._input = input

    @property
    def output(self):
        """Gets the output of this CommonCreateTaskReq.


        :return: The output of this CommonCreateTaskReq.
        :rtype: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this CommonCreateTaskReq.


        :param output: The output of this CommonCreateTaskReq.
        :type output: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
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
        :type user_data: str
        """
        self._user_data = user_data

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
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CommonCreateTaskReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
