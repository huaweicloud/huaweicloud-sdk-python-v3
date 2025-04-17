# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Condition:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'instance_name': 'ResourceNameItem',
        'tag': 'ResourceGroupTagRelation'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'instance_name': 'instance_name',
        'tag': 'tag'
    }

    def __init__(self, enterprise_project_id=None, instance_name=None, tag=None):
        r"""Condition

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 企业项目ID
        :type enterprise_project_id: str
        :param instance_name: 
        :type instance_name: :class:`huaweicloudsdkces.v2.ResourceNameItem`
        :param tag: 
        :type tag: :class:`huaweicloudsdkces.v2.ResourceGroupTagRelation`
        """
        
        

        self._enterprise_project_id = None
        self._instance_name = None
        self._tag = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if instance_name is not None:
            self.instance_name = instance_name
        if tag is not None:
            self.tag = tag

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this Condition.

        企业项目ID

        :return: The enterprise_project_id of this Condition.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this Condition.

        企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this Condition.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def instance_name(self):
        r"""Gets the instance_name of this Condition.

        :return: The instance_name of this Condition.
        :rtype: :class:`huaweicloudsdkces.v2.ResourceNameItem`
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this Condition.

        :param instance_name: The instance_name of this Condition.
        :type instance_name: :class:`huaweicloudsdkces.v2.ResourceNameItem`
        """
        self._instance_name = instance_name

    @property
    def tag(self):
        r"""Gets the tag of this Condition.

        :return: The tag of this Condition.
        :rtype: :class:`huaweicloudsdkces.v2.ResourceGroupTagRelation`
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        r"""Sets the tag of this Condition.

        :param tag: The tag of this Condition.
        :type tag: :class:`huaweicloudsdkces.v2.ResourceGroupTagRelation`
        """
        self._tag = tag

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
        if not isinstance(other, Condition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
