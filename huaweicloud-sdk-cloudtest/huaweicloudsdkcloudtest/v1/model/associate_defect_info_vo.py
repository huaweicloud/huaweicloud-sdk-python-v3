# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssociateDefectInfoVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'associate': 'bool',
        'associate_count': 'int'
    }

    attribute_map = {
        'associate': 'associate',
        'associate_count': 'associate_count'
    }

    def __init__(self, associate=None, associate_count=None):
        """AssociateDefectInfoVo

        The model defined in huaweicloud sdk

        :param associate: 是否已关联
        :type associate: bool
        :param associate_count: 关联缺陷数
        :type associate_count: int
        """
        
        

        self._associate = None
        self._associate_count = None
        self.discriminator = None

        if associate is not None:
            self.associate = associate
        if associate_count is not None:
            self.associate_count = associate_count

    @property
    def associate(self):
        """Gets the associate of this AssociateDefectInfoVo.

        是否已关联

        :return: The associate of this AssociateDefectInfoVo.
        :rtype: bool
        """
        return self._associate

    @associate.setter
    def associate(self, associate):
        """Sets the associate of this AssociateDefectInfoVo.

        是否已关联

        :param associate: The associate of this AssociateDefectInfoVo.
        :type associate: bool
        """
        self._associate = associate

    @property
    def associate_count(self):
        """Gets the associate_count of this AssociateDefectInfoVo.

        关联缺陷数

        :return: The associate_count of this AssociateDefectInfoVo.
        :rtype: int
        """
        return self._associate_count

    @associate_count.setter
    def associate_count(self, associate_count):
        """Sets the associate_count of this AssociateDefectInfoVo.

        关联缺陷数

        :param associate_count: The associate_count of this AssociateDefectInfoVo.
        :type associate_count: int
        """
        self._associate_count = associate_count

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
        if not isinstance(other, AssociateDefectInfoVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
