# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ErInfo:

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
        'name': 'str'
    }

    attribute_map = {
        'er_id': 'er_id',
        'name': 'name'
    }

    def __init__(self, er_id=None, name=None):
        r"""ErInfo

        The model defined in huaweicloud sdk

        :param er_id: **参数解释**： 企业路由器ID **取值范围**： 不涉及
        :type er_id: str
        :param name: **参数解释**： 企业路由器名称 **取值范围**： 不涉及
        :type name: str
        """
        
        

        self._er_id = None
        self._name = None
        self.discriminator = None

        if er_id is not None:
            self.er_id = er_id
        if name is not None:
            self.name = name

    @property
    def er_id(self):
        r"""Gets the er_id of this ErInfo.

        **参数解释**： 企业路由器ID **取值范围**： 不涉及

        :return: The er_id of this ErInfo.
        :rtype: str
        """
        return self._er_id

    @er_id.setter
    def er_id(self, er_id):
        r"""Sets the er_id of this ErInfo.

        **参数解释**： 企业路由器ID **取值范围**： 不涉及

        :param er_id: The er_id of this ErInfo.
        :type er_id: str
        """
        self._er_id = er_id

    @property
    def name(self):
        r"""Gets the name of this ErInfo.

        **参数解释**： 企业路由器名称 **取值范围**： 不涉及

        :return: The name of this ErInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ErInfo.

        **参数解释**： 企业路由器名称 **取值范围**： 不涉及

        :param name: The name of this ErInfo.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, ErInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
