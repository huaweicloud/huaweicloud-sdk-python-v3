# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VpcDetail:

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
        'cidr': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'cidr': 'cidr'
    }

    def __init__(self, id=None, name=None, cidr=None):
        r"""VpcDetail

        The model defined in huaweicloud sdk

        :param id: 创建引流VPC产生的随机UUID
        :type id: str
        :param name: 引流VPC名称
        :type name: str
        :param cidr: 功能说明：虚拟私有云下可用子网的范围 取值范围： 10.0.0.0/8~24 172.16.0.0/12~24 192.168.0.0/16~24 不指定cidr时，默认值为空 约束：必须是cidr格式，例如:192.168.0.0/16
        :type cidr: str
        """
        
        

        self._id = None
        self._name = None
        self._cidr = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if cidr is not None:
            self.cidr = cidr

    @property
    def id(self):
        r"""Gets the id of this VpcDetail.

        创建引流VPC产生的随机UUID

        :return: The id of this VpcDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this VpcDetail.

        创建引流VPC产生的随机UUID

        :param id: The id of this VpcDetail.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this VpcDetail.

        引流VPC名称

        :return: The name of this VpcDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this VpcDetail.

        引流VPC名称

        :param name: The name of this VpcDetail.
        :type name: str
        """
        self._name = name

    @property
    def cidr(self):
        r"""Gets the cidr of this VpcDetail.

        功能说明：虚拟私有云下可用子网的范围 取值范围： 10.0.0.0/8~24 172.16.0.0/12~24 192.168.0.0/16~24 不指定cidr时，默认值为空 约束：必须是cidr格式，例如:192.168.0.0/16

        :return: The cidr of this VpcDetail.
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        r"""Sets the cidr of this VpcDetail.

        功能说明：虚拟私有云下可用子网的范围 取值范围： 10.0.0.0/8~24 172.16.0.0/12~24 192.168.0.0/16~24 不指定cidr时，默认值为空 约束：必须是cidr格式，例如:192.168.0.0/16

        :param cidr: The cidr of this VpcDetail.
        :type cidr: str
        """
        self._cidr = cidr

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
        if not isinstance(other, VpcDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
