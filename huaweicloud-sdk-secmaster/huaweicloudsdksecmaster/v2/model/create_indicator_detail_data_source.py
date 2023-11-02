# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateIndicatorDetailDataSource:

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
        'product_name': 'str',
        'product_feature': 'str'
    }

    attribute_map = {
        'source_type': 'source_type',
        'domain_id': 'domain_id',
        'project_id': 'project_id',
        'region_id': 'region_id',
        'product_name': 'product_name',
        'product_feature': 'product_feature'
    }

    def __init__(self, source_type=None, domain_id=None, project_id=None, region_id=None, product_name=None, product_feature=None):
        """CreateIndicatorDetailDataSource

        The model defined in huaweicloud sdk

        :param source_type: current page count
        :type source_type: int
        :param domain_id: Id value
        :type domain_id: str
        :param project_id: Id value
        :type project_id: str
        :param region_id: Id value
        :type region_id: str
        :param product_name: Id value
        :type product_name: str
        :param product_feature: Id value
        :type product_feature: str
        """
        
        

        self._source_type = None
        self._domain_id = None
        self._project_id = None
        self._region_id = None
        self._product_name = None
        self._product_feature = None
        self.discriminator = None

        self.source_type = source_type
        self.domain_id = domain_id
        self.project_id = project_id
        self.region_id = region_id
        self.product_name = product_name
        self.product_feature = product_feature

    @property
    def source_type(self):
        """Gets the source_type of this CreateIndicatorDetailDataSource.

        current page count

        :return: The source_type of this CreateIndicatorDetailDataSource.
        :rtype: int
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """Sets the source_type of this CreateIndicatorDetailDataSource.

        current page count

        :param source_type: The source_type of this CreateIndicatorDetailDataSource.
        :type source_type: int
        """
        self._source_type = source_type

    @property
    def domain_id(self):
        """Gets the domain_id of this CreateIndicatorDetailDataSource.

        Id value

        :return: The domain_id of this CreateIndicatorDetailDataSource.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this CreateIndicatorDetailDataSource.

        Id value

        :param domain_id: The domain_id of this CreateIndicatorDetailDataSource.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def project_id(self):
        """Gets the project_id of this CreateIndicatorDetailDataSource.

        Id value

        :return: The project_id of this CreateIndicatorDetailDataSource.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CreateIndicatorDetailDataSource.

        Id value

        :param project_id: The project_id of this CreateIndicatorDetailDataSource.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def region_id(self):
        """Gets the region_id of this CreateIndicatorDetailDataSource.

        Id value

        :return: The region_id of this CreateIndicatorDetailDataSource.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this CreateIndicatorDetailDataSource.

        Id value

        :param region_id: The region_id of this CreateIndicatorDetailDataSource.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def product_name(self):
        """Gets the product_name of this CreateIndicatorDetailDataSource.

        Id value

        :return: The product_name of this CreateIndicatorDetailDataSource.
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """Sets the product_name of this CreateIndicatorDetailDataSource.

        Id value

        :param product_name: The product_name of this CreateIndicatorDetailDataSource.
        :type product_name: str
        """
        self._product_name = product_name

    @property
    def product_feature(self):
        """Gets the product_feature of this CreateIndicatorDetailDataSource.

        Id value

        :return: The product_feature of this CreateIndicatorDetailDataSource.
        :rtype: str
        """
        return self._product_feature

    @product_feature.setter
    def product_feature(self, product_feature):
        """Sets the product_feature of this CreateIndicatorDetailDataSource.

        Id value

        :param product_feature: The product_feature of this CreateIndicatorDetailDataSource.
        :type product_feature: str
        """
        self._product_feature = product_feature

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
        if not isinstance(other, CreateIndicatorDetailDataSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
