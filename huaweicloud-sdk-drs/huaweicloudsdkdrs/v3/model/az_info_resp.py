# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AzInfoResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'code': 'str',
        'name': 'str',
        'status': 'str'
    }

    attribute_map = {
        'code': 'code',
        'name': 'name',
        'status': 'status'
    }

    def __init__(self, code=None, name=None, status=None):
        r"""AzInfoResp

        The model defined in huaweicloud sdk

        :param code: 可用区标识代码
        :type code: str
        :param name: 可用区名称
        :type name: str
        :param status: 可用区状态
        :type status: str
        """
        
        

        self._code = None
        self._name = None
        self._status = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status

    @property
    def code(self):
        r"""Gets the code of this AzInfoResp.

        可用区标识代码

        :return: The code of this AzInfoResp.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this AzInfoResp.

        可用区标识代码

        :param code: The code of this AzInfoResp.
        :type code: str
        """
        self._code = code

    @property
    def name(self):
        r"""Gets the name of this AzInfoResp.

        可用区名称

        :return: The name of this AzInfoResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AzInfoResp.

        可用区名称

        :param name: The name of this AzInfoResp.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this AzInfoResp.

        可用区状态

        :return: The status of this AzInfoResp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this AzInfoResp.

        可用区状态

        :param status: The status of this AzInfoResp.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, AzInfoResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
