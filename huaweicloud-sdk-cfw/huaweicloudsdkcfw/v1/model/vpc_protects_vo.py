# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VPCProtectsVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'self_total': 'int',
        'other_total': 'int',
        'protect_vpcs': 'list[VpcAttachmentDetail]',
        'self_protect_vpcs': 'list[VpcAttachmentDetail]',
        'other_protect_vpcs': 'list[VpcAttachmentDetail]'
    }

    attribute_map = {
        'total': 'total',
        'self_total': 'self_total',
        'other_total': 'other_total',
        'protect_vpcs': 'protect_vpcs',
        'self_protect_vpcs': 'self_protect_vpcs',
        'other_protect_vpcs': 'other_protect_vpcs'
    }

    def __init__(self, total=None, self_total=None, other_total=None, protect_vpcs=None, self_protect_vpcs=None, other_protect_vpcs=None):
        """VPCProtectsVo

        The model defined in huaweicloud sdk

        :param total: 总VPC数
        :type total: int
        :param self_total: 本项目防护VPC数
        :type self_total: int
        :param other_total: 其他项目防护VPC数
        :type other_total: int
        :param protect_vpcs: 防护VPC
        :type protect_vpcs: list[:class:`huaweicloudsdkcfw.v1.VpcAttachmentDetail`]
        :param self_protect_vpcs: 本项目防护VPC
        :type self_protect_vpcs: list[:class:`huaweicloudsdkcfw.v1.VpcAttachmentDetail`]
        :param other_protect_vpcs: 其他项目防护VPC
        :type other_protect_vpcs: list[:class:`huaweicloudsdkcfw.v1.VpcAttachmentDetail`]
        """
        
        

        self._total = None
        self._self_total = None
        self._other_total = None
        self._protect_vpcs = None
        self._self_protect_vpcs = None
        self._other_protect_vpcs = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if self_total is not None:
            self.self_total = self_total
        if other_total is not None:
            self.other_total = other_total
        if protect_vpcs is not None:
            self.protect_vpcs = protect_vpcs
        if self_protect_vpcs is not None:
            self.self_protect_vpcs = self_protect_vpcs
        if other_protect_vpcs is not None:
            self.other_protect_vpcs = other_protect_vpcs

    @property
    def total(self):
        """Gets the total of this VPCProtectsVo.

        总VPC数

        :return: The total of this VPCProtectsVo.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this VPCProtectsVo.

        总VPC数

        :param total: The total of this VPCProtectsVo.
        :type total: int
        """
        self._total = total

    @property
    def self_total(self):
        """Gets the self_total of this VPCProtectsVo.

        本项目防护VPC数

        :return: The self_total of this VPCProtectsVo.
        :rtype: int
        """
        return self._self_total

    @self_total.setter
    def self_total(self, self_total):
        """Sets the self_total of this VPCProtectsVo.

        本项目防护VPC数

        :param self_total: The self_total of this VPCProtectsVo.
        :type self_total: int
        """
        self._self_total = self_total

    @property
    def other_total(self):
        """Gets the other_total of this VPCProtectsVo.

        其他项目防护VPC数

        :return: The other_total of this VPCProtectsVo.
        :rtype: int
        """
        return self._other_total

    @other_total.setter
    def other_total(self, other_total):
        """Sets the other_total of this VPCProtectsVo.

        其他项目防护VPC数

        :param other_total: The other_total of this VPCProtectsVo.
        :type other_total: int
        """
        self._other_total = other_total

    @property
    def protect_vpcs(self):
        """Gets the protect_vpcs of this VPCProtectsVo.

        防护VPC

        :return: The protect_vpcs of this VPCProtectsVo.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.VpcAttachmentDetail`]
        """
        return self._protect_vpcs

    @protect_vpcs.setter
    def protect_vpcs(self, protect_vpcs):
        """Sets the protect_vpcs of this VPCProtectsVo.

        防护VPC

        :param protect_vpcs: The protect_vpcs of this VPCProtectsVo.
        :type protect_vpcs: list[:class:`huaweicloudsdkcfw.v1.VpcAttachmentDetail`]
        """
        self._protect_vpcs = protect_vpcs

    @property
    def self_protect_vpcs(self):
        """Gets the self_protect_vpcs of this VPCProtectsVo.

        本项目防护VPC

        :return: The self_protect_vpcs of this VPCProtectsVo.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.VpcAttachmentDetail`]
        """
        return self._self_protect_vpcs

    @self_protect_vpcs.setter
    def self_protect_vpcs(self, self_protect_vpcs):
        """Sets the self_protect_vpcs of this VPCProtectsVo.

        本项目防护VPC

        :param self_protect_vpcs: The self_protect_vpcs of this VPCProtectsVo.
        :type self_protect_vpcs: list[:class:`huaweicloudsdkcfw.v1.VpcAttachmentDetail`]
        """
        self._self_protect_vpcs = self_protect_vpcs

    @property
    def other_protect_vpcs(self):
        """Gets the other_protect_vpcs of this VPCProtectsVo.

        其他项目防护VPC

        :return: The other_protect_vpcs of this VPCProtectsVo.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.VpcAttachmentDetail`]
        """
        return self._other_protect_vpcs

    @other_protect_vpcs.setter
    def other_protect_vpcs(self, other_protect_vpcs):
        """Sets the other_protect_vpcs of this VPCProtectsVo.

        其他项目防护VPC

        :param other_protect_vpcs: The other_protect_vpcs of this VPCProtectsVo.
        :type other_protect_vpcs: list[:class:`huaweicloudsdkcfw.v1.VpcAttachmentDetail`]
        """
        self._other_protect_vpcs = other_protect_vpcs

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
        if not isinstance(other, VPCProtectsVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
