# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Storage:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'az_status': 'dict(str, str)'
    }

    attribute_map = {
        'name': 'name',
        'az_status': 'az_status'
    }

    def __init__(self, name=None, az_status=None):
        r"""Storage

        The model defined in huaweicloud sdk

        :param name: 磁盘类型名称，可能取值如下： - ULTRAHIGH，表示SSD。
        :type name: str
        :param az_status: 其中key是可用区编号，value是规格所在az的状态，包含以下状态： - normal，在售。 - unsupported，暂不支持该规格。 - sellout，售罄。
        :type az_status: dict(str, str)
        """
        
        

        self._name = None
        self._az_status = None
        self.discriminator = None

        self.name = name
        self.az_status = az_status

    @property
    def name(self):
        r"""Gets the name of this Storage.

        磁盘类型名称，可能取值如下： - ULTRAHIGH，表示SSD。

        :return: The name of this Storage.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Storage.

        磁盘类型名称，可能取值如下： - ULTRAHIGH，表示SSD。

        :param name: The name of this Storage.
        :type name: str
        """
        self._name = name

    @property
    def az_status(self):
        r"""Gets the az_status of this Storage.

        其中key是可用区编号，value是规格所在az的状态，包含以下状态： - normal，在售。 - unsupported，暂不支持该规格。 - sellout，售罄。

        :return: The az_status of this Storage.
        :rtype: dict(str, str)
        """
        return self._az_status

    @az_status.setter
    def az_status(self, az_status):
        r"""Sets the az_status of this Storage.

        其中key是可用区编号，value是规格所在az的状态，包含以下状态： - normal，在售。 - unsupported，暂不支持该规格。 - sellout，售罄。

        :param az_status: The az_status of this Storage.
        :type az_status: dict(str, str)
        """
        self._az_status = az_status

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
        if not isinstance(other, Storage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
