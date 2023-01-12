# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProductInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_id': 'str',
        'project_id': 'str',
        'region': 'str',
        'company_name': 'str',
        'product_name': 'str'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'project_id': 'project_id',
        'region': 'region',
        'company_name': 'company_name',
        'product_name': 'product_name'
    }

    def __init__(self, domain_id=None, project_id=None, region=None, company_name=None, product_name=None):
        """ProductInfo

        The model defined in huaweicloud sdk

        :param domain_id: 数据源产品所属账号的ID。
        :type domain_id: str
        :param project_id: 数据源产品所属项目的ID。
        :type project_id: str
        :param region: 数据源产品所在区域。
        :type region: str
        :param company_name: 数据源产品所属公司的名称。
        :type company_name: str
        :param product_name: 数据源产品的名称。
        :type product_name: str
        """
        
        

        self._domain_id = None
        self._project_id = None
        self._region = None
        self._company_name = None
        self._product_name = None
        self.discriminator = None

        self.domain_id = domain_id
        self.project_id = project_id
        self.region = region
        self.company_name = company_name
        self.product_name = product_name

    @property
    def domain_id(self):
        """Gets the domain_id of this ProductInfo.

        数据源产品所属账号的ID。

        :return: The domain_id of this ProductInfo.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this ProductInfo.

        数据源产品所属账号的ID。

        :param domain_id: The domain_id of this ProductInfo.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def project_id(self):
        """Gets the project_id of this ProductInfo.

        数据源产品所属项目的ID。

        :return: The project_id of this ProductInfo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ProductInfo.

        数据源产品所属项目的ID。

        :param project_id: The project_id of this ProductInfo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def region(self):
        """Gets the region of this ProductInfo.

        数据源产品所在区域。

        :return: The region of this ProductInfo.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ProductInfo.

        数据源产品所在区域。

        :param region: The region of this ProductInfo.
        :type region: str
        """
        self._region = region

    @property
    def company_name(self):
        """Gets the company_name of this ProductInfo.

        数据源产品所属公司的名称。

        :return: The company_name of this ProductInfo.
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this ProductInfo.

        数据源产品所属公司的名称。

        :param company_name: The company_name of this ProductInfo.
        :type company_name: str
        """
        self._company_name = company_name

    @property
    def product_name(self):
        """Gets the product_name of this ProductInfo.

        数据源产品的名称。

        :return: The product_name of this ProductInfo.
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """Sets the product_name of this ProductInfo.

        数据源产品的名称。

        :param product_name: The product_name of this ProductInfo.
        :type product_name: str
        """
        self._product_name = product_name

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
        if not isinstance(other, ProductInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
