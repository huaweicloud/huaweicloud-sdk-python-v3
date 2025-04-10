# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Er:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'er_id': 'str',
        'er_attach_id': 'str'
    }

    attribute_map = {
        'er_id': 'er_id',
        'er_attach_id': 'er_attach_id'
    }

    def __init__(self, er_id=None, er_attach_id=None):
        r"""Er

        The model defined in huaweicloud sdk

        :param er_id: ER ID，创建东西向防护引用的 ID
        :type er_id: str
        :param er_attach_id: 企业路由器连接id，该连接用于连接防火墙和企业路由器，此字段可在通过id在ER界面查询指定er后在管理连接界面查询连接了解连接具体情况。
        :type er_attach_id: str
        """
        
        

        self._er_id = None
        self._er_attach_id = None
        self.discriminator = None

        if er_id is not None:
            self.er_id = er_id
        if er_attach_id is not None:
            self.er_attach_id = er_attach_id

    @property
    def er_id(self):
        r"""Gets the er_id of this Er.

        ER ID，创建东西向防护引用的 ID

        :return: The er_id of this Er.
        :rtype: str
        """
        return self._er_id

    @er_id.setter
    def er_id(self, er_id):
        r"""Sets the er_id of this Er.

        ER ID，创建东西向防护引用的 ID

        :param er_id: The er_id of this Er.
        :type er_id: str
        """
        self._er_id = er_id

    @property
    def er_attach_id(self):
        r"""Gets the er_attach_id of this Er.

        企业路由器连接id，该连接用于连接防火墙和企业路由器，此字段可在通过id在ER界面查询指定er后在管理连接界面查询连接了解连接具体情况。

        :return: The er_attach_id of this Er.
        :rtype: str
        """
        return self._er_attach_id

    @er_attach_id.setter
    def er_attach_id(self, er_attach_id):
        r"""Sets the er_attach_id of this Er.

        企业路由器连接id，该连接用于连接防火墙和企业路由器，此字段可在通过id在ER界面查询指定er后在管理连接界面查询连接了解连接具体情况。

        :param er_attach_id: The er_attach_id of this Er.
        :type er_attach_id: str
        """
        self._er_attach_id = er_attach_id

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
        if not isinstance(other, Er):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
