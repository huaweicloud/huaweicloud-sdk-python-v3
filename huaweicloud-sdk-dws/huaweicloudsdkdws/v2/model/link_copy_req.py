# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LinkCopyReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'backup_name': 'str',
        'description': 'str'
    }

    attribute_map = {
        'backup_name': 'backup_name',
        'description': 'description'
    }

    def __init__(self, backup_name=None, description=None):
        r"""LinkCopyReq

        The model defined in huaweicloud sdk

        :param backup_name: **参数解释**： 快照名称。 **取值范围**： 不涉及。
        :type backup_name: str
        :param description: **参数解释**： 描述信息。 **取值范围**： 不涉及。
        :type description: str
        """
        
        

        self._backup_name = None
        self._description = None
        self.discriminator = None

        self.backup_name = backup_name
        if description is not None:
            self.description = description

    @property
    def backup_name(self):
        r"""Gets the backup_name of this LinkCopyReq.

        **参数解释**： 快照名称。 **取值范围**： 不涉及。

        :return: The backup_name of this LinkCopyReq.
        :rtype: str
        """
        return self._backup_name

    @backup_name.setter
    def backup_name(self, backup_name):
        r"""Sets the backup_name of this LinkCopyReq.

        **参数解释**： 快照名称。 **取值范围**： 不涉及。

        :param backup_name: The backup_name of this LinkCopyReq.
        :type backup_name: str
        """
        self._backup_name = backup_name

    @property
    def description(self):
        r"""Gets the description of this LinkCopyReq.

        **参数解释**： 描述信息。 **取值范围**： 不涉及。

        :return: The description of this LinkCopyReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this LinkCopyReq.

        **参数解释**： 描述信息。 **取值范围**： 不涉及。

        :param description: The description of this LinkCopyReq.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, LinkCopyReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
