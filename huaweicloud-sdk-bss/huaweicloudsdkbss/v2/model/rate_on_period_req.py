# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RateOnPeriodReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'product_infos': 'list[PeriodProductInfo]'
    }

    attribute_map = {
        'project_id': 'project_id',
        'product_infos': 'product_infos'
    }

    def __init__(self, project_id=None, product_infos=None):
        """RateOnPeriodReq

        The model defined in huaweicloud sdk

        :param project_id: 项目ID。  说明： 获取方法： 步骤1：调用IAM获取委托Token接口，获取客户Token。步骤2：参见如何将合作伙伴Token置换为客户Token的步骤2，获取项目ID。IAM子用户调用此接口，需要IAM主账号授权，具体请参考创建用户组并授权。
        :type project_id: str
        :param product_infos: 产品信息列表，询价时要询价产品的信息的列表，具体参见表1。
        :type product_infos: list[:class:`huaweicloudsdkbss.v2.PeriodProductInfo`]
        """
        
        

        self._project_id = None
        self._product_infos = None
        self.discriminator = None

        self.project_id = project_id
        self.product_infos = product_infos

    @property
    def project_id(self):
        """Gets the project_id of this RateOnPeriodReq.

        项目ID。  说明： 获取方法： 步骤1：调用IAM获取委托Token接口，获取客户Token。步骤2：参见如何将合作伙伴Token置换为客户Token的步骤2，获取项目ID。IAM子用户调用此接口，需要IAM主账号授权，具体请参考创建用户组并授权。

        :return: The project_id of this RateOnPeriodReq.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this RateOnPeriodReq.

        项目ID。  说明： 获取方法： 步骤1：调用IAM获取委托Token接口，获取客户Token。步骤2：参见如何将合作伙伴Token置换为客户Token的步骤2，获取项目ID。IAM子用户调用此接口，需要IAM主账号授权，具体请参考创建用户组并授权。

        :param project_id: The project_id of this RateOnPeriodReq.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def product_infos(self):
        """Gets the product_infos of this RateOnPeriodReq.

        产品信息列表，询价时要询价产品的信息的列表，具体参见表1。

        :return: The product_infos of this RateOnPeriodReq.
        :rtype: list[:class:`huaweicloudsdkbss.v2.PeriodProductInfo`]
        """
        return self._product_infos

    @product_infos.setter
    def product_infos(self, product_infos):
        """Sets the product_infos of this RateOnPeriodReq.

        产品信息列表，询价时要询价产品的信息的列表，具体参见表1。

        :param product_infos: The product_infos of this RateOnPeriodReq.
        :type product_infos: list[:class:`huaweicloudsdkbss.v2.PeriodProductInfo`]
        """
        self._product_infos = product_infos

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
        if not isinstance(other, RateOnPeriodReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
