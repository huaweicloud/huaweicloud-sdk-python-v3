# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlertDataSource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source_type': 'int',
        'domain_id': 'str',
        'project_id': 'str',
        'region_id': 'str',
        'company_name': 'str',
        'product_name': 'str',
        'product_feature': 'str',
        'product_module': 'str'
    }

    attribute_map = {
        'source_type': 'source_type',
        'domain_id': 'domain_id',
        'project_id': 'project_id',
        'region_id': 'region_id',
        'company_name': 'company_name',
        'product_name': 'product_name',
        'product_feature': 'product_feature',
        'product_module': 'product_module'
    }

    def __init__(self, source_type=None, domain_id=None, project_id=None, region_id=None, company_name=None, product_name=None, product_feature=None, product_module=None):
        """AlertDataSource

        The model defined in huaweicloud sdk

        :param source_type: 数据源类型，取值范围如下： 1 - 华为产品 2 - 第三方产品 3 - 租户私有产品
        :type source_type: int
        :param domain_id: 数据源产品所属账号的id
        :type domain_id: str
        :param project_id: 数据源产品所属项目的id
        :type project_id: str
        :param region_id: 数据源产品所在区域，具体取值范围查看华为云地区和终端节点定义，例如cn-north-1
        :type region_id: str
        :param company_name: 数据源产品所属公司的名称
        :type company_name: str
        :param product_name: 数据源产品的名称
        :type product_name: str
        :param product_feature: 产品功能特性名称，用来指明检测到当前事件的产品的功能特性
        :type product_feature: str
        :param product_module: 检测模块列表
        :type product_module: str
        """
        
        

        self._source_type = None
        self._domain_id = None
        self._project_id = None
        self._region_id = None
        self._company_name = None
        self._product_name = None
        self._product_feature = None
        self._product_module = None
        self.discriminator = None

        if source_type is not None:
            self.source_type = source_type
        if domain_id is not None:
            self.domain_id = domain_id
        if project_id is not None:
            self.project_id = project_id
        if region_id is not None:
            self.region_id = region_id
        if company_name is not None:
            self.company_name = company_name
        if product_name is not None:
            self.product_name = product_name
        if product_feature is not None:
            self.product_feature = product_feature
        if product_module is not None:
            self.product_module = product_module

    @property
    def source_type(self):
        """Gets the source_type of this AlertDataSource.

        数据源类型，取值范围如下： 1 - 华为产品 2 - 第三方产品 3 - 租户私有产品

        :return: The source_type of this AlertDataSource.
        :rtype: int
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """Sets the source_type of this AlertDataSource.

        数据源类型，取值范围如下： 1 - 华为产品 2 - 第三方产品 3 - 租户私有产品

        :param source_type: The source_type of this AlertDataSource.
        :type source_type: int
        """
        self._source_type = source_type

    @property
    def domain_id(self):
        """Gets the domain_id of this AlertDataSource.

        数据源产品所属账号的id

        :return: The domain_id of this AlertDataSource.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this AlertDataSource.

        数据源产品所属账号的id

        :param domain_id: The domain_id of this AlertDataSource.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def project_id(self):
        """Gets the project_id of this AlertDataSource.

        数据源产品所属项目的id

        :return: The project_id of this AlertDataSource.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this AlertDataSource.

        数据源产品所属项目的id

        :param project_id: The project_id of this AlertDataSource.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def region_id(self):
        """Gets the region_id of this AlertDataSource.

        数据源产品所在区域，具体取值范围查看华为云地区和终端节点定义，例如cn-north-1

        :return: The region_id of this AlertDataSource.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this AlertDataSource.

        数据源产品所在区域，具体取值范围查看华为云地区和终端节点定义，例如cn-north-1

        :param region_id: The region_id of this AlertDataSource.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def company_name(self):
        """Gets the company_name of this AlertDataSource.

        数据源产品所属公司的名称

        :return: The company_name of this AlertDataSource.
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this AlertDataSource.

        数据源产品所属公司的名称

        :param company_name: The company_name of this AlertDataSource.
        :type company_name: str
        """
        self._company_name = company_name

    @property
    def product_name(self):
        """Gets the product_name of this AlertDataSource.

        数据源产品的名称

        :return: The product_name of this AlertDataSource.
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """Sets the product_name of this AlertDataSource.

        数据源产品的名称

        :param product_name: The product_name of this AlertDataSource.
        :type product_name: str
        """
        self._product_name = product_name

    @property
    def product_feature(self):
        """Gets the product_feature of this AlertDataSource.

        产品功能特性名称，用来指明检测到当前事件的产品的功能特性

        :return: The product_feature of this AlertDataSource.
        :rtype: str
        """
        return self._product_feature

    @product_feature.setter
    def product_feature(self, product_feature):
        """Sets the product_feature of this AlertDataSource.

        产品功能特性名称，用来指明检测到当前事件的产品的功能特性

        :param product_feature: The product_feature of this AlertDataSource.
        :type product_feature: str
        """
        self._product_feature = product_feature

    @property
    def product_module(self):
        """Gets the product_module of this AlertDataSource.

        检测模块列表

        :return: The product_module of this AlertDataSource.
        :rtype: str
        """
        return self._product_module

    @product_module.setter
    def product_module(self, product_module):
        """Sets the product_module of this AlertDataSource.

        检测模块列表

        :param product_module: The product_module of this AlertDataSource.
        :type product_module: str
        """
        self._product_module = product_module

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
        if not isinstance(other, AlertDataSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
