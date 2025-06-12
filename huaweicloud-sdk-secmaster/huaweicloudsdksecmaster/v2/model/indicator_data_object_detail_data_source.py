# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IndicatorDataObjectDetailDataSource:

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
        'region_id': 'str'
    }

    attribute_map = {
        'source_type': 'source_type',
        'domain_id': 'domain_id',
        'project_id': 'project_id',
        'region_id': 'region_id'
    }

    def __init__(self, source_type=None, domain_id=None, project_id=None, region_id=None):
        r"""IndicatorDataObjectDetailDataSource

        The model defined in huaweicloud sdk

        :param source_type: 数据源类型，取值范围如下：1 - 云上产品 2 - 第三方产品 3 - 租户私有产品
        :type source_type: int
        :param domain_id: 租户ID
        :type domain_id: str
        :param project_id: 项目ID
        :type project_id: str
        :param region_id: 区域ID
        :type region_id: str
        """
        
        

        self._source_type = None
        self._domain_id = None
        self._project_id = None
        self._region_id = None
        self.discriminator = None

        if source_type is not None:
            self.source_type = source_type
        if domain_id is not None:
            self.domain_id = domain_id
        if project_id is not None:
            self.project_id = project_id
        if region_id is not None:
            self.region_id = region_id

    @property
    def source_type(self):
        r"""Gets the source_type of this IndicatorDataObjectDetailDataSource.

        数据源类型，取值范围如下：1 - 云上产品 2 - 第三方产品 3 - 租户私有产品

        :return: The source_type of this IndicatorDataObjectDetailDataSource.
        :rtype: int
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        r"""Sets the source_type of this IndicatorDataObjectDetailDataSource.

        数据源类型，取值范围如下：1 - 云上产品 2 - 第三方产品 3 - 租户私有产品

        :param source_type: The source_type of this IndicatorDataObjectDetailDataSource.
        :type source_type: int
        """
        self._source_type = source_type

    @property
    def domain_id(self):
        r"""Gets the domain_id of this IndicatorDataObjectDetailDataSource.

        租户ID

        :return: The domain_id of this IndicatorDataObjectDetailDataSource.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this IndicatorDataObjectDetailDataSource.

        租户ID

        :param domain_id: The domain_id of this IndicatorDataObjectDetailDataSource.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def project_id(self):
        r"""Gets the project_id of this IndicatorDataObjectDetailDataSource.

        项目ID

        :return: The project_id of this IndicatorDataObjectDetailDataSource.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this IndicatorDataObjectDetailDataSource.

        项目ID

        :param project_id: The project_id of this IndicatorDataObjectDetailDataSource.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def region_id(self):
        r"""Gets the region_id of this IndicatorDataObjectDetailDataSource.

        区域ID

        :return: The region_id of this IndicatorDataObjectDetailDataSource.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this IndicatorDataObjectDetailDataSource.

        区域ID

        :param region_id: The region_id of this IndicatorDataObjectDetailDataSource.
        :type region_id: str
        """
        self._region_id = region_id

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
        if not isinstance(other, IndicatorDataObjectDetailDataSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
