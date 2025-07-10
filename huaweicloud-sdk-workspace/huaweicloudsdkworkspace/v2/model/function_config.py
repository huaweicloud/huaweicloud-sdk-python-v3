# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FunctionConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'status': 'str',
        'values': 'list[MapObject]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'values': 'values'
    }

    def __init__(self, id=None, name=None, status=None, values=None):
        r"""FunctionConfig

        The model defined in huaweicloud sdk

        :param id: 功能配置id。
        :type id: str
        :param name: 功能配置名称。
        :type name: str
        :param status: 功能配置开关的状态，表示开启还是关闭 ON/OFF。 - ON： 开启该功能 - OFF： 关闭该功能。
        :type status: str
        :param values: 配置项列表，键值对格式。
        :type values: list[:class:`huaweicloudsdkworkspace.v2.MapObject`]
        """
        
        

        self._id = None
        self._name = None
        self._status = None
        self._values = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if values is not None:
            self.values = values

    @property
    def id(self):
        r"""Gets the id of this FunctionConfig.

        功能配置id。

        :return: The id of this FunctionConfig.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this FunctionConfig.

        功能配置id。

        :param id: The id of this FunctionConfig.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this FunctionConfig.

        功能配置名称。

        :return: The name of this FunctionConfig.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this FunctionConfig.

        功能配置名称。

        :param name: The name of this FunctionConfig.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this FunctionConfig.

        功能配置开关的状态，表示开启还是关闭 ON/OFF。 - ON： 开启该功能 - OFF： 关闭该功能。

        :return: The status of this FunctionConfig.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this FunctionConfig.

        功能配置开关的状态，表示开启还是关闭 ON/OFF。 - ON： 开启该功能 - OFF： 关闭该功能。

        :param status: The status of this FunctionConfig.
        :type status: str
        """
        self._status = status

    @property
    def values(self):
        r"""Gets the values of this FunctionConfig.

        配置项列表，键值对格式。

        :return: The values of this FunctionConfig.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.MapObject`]
        """
        return self._values

    @values.setter
    def values(self, values):
        r"""Sets the values of this FunctionConfig.

        配置项列表，键值对格式。

        :param values: The values of this FunctionConfig.
        :type values: list[:class:`huaweicloudsdkworkspace.v2.MapObject`]
        """
        self._values = values

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
        if not isinstance(other, FunctionConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
