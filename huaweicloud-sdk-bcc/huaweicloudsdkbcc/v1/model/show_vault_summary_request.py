# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowVaultSummaryRequest:

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
        'region_id': 'str',
        'enterprise_project_id': 'str',
        'start_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'region_id': 'region_id',
        'enterprise_project_id': 'enterprise_project_id',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, domain_id=None, region_id=None, enterprise_project_id=None, start_time=None, end_time=None):
        r"""ShowVaultSummaryRequest

        The model defined in huaweicloud sdk

        :param domain_id: 账号ID
        :type domain_id: str
        :param region_id: 区域regionId
        :type region_id: str
        :param enterprise_project_id: 企业项目Id
        :type enterprise_project_id: str
        :param start_time: 开始时间,格式为“yyyy-mm-ddThh:mm:ssZ”
        :type start_time: str
        :param end_time: 结束时间,格式为“yyyy-mm-ddThh:mm:ssZ”
        :type end_time: str
        """
        
        

        self._domain_id = None
        self._region_id = None
        self._enterprise_project_id = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        self.domain_id = domain_id
        if region_id is not None:
            self.region_id = region_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ShowVaultSummaryRequest.

        账号ID

        :return: The domain_id of this ShowVaultSummaryRequest.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ShowVaultSummaryRequest.

        账号ID

        :param domain_id: The domain_id of this ShowVaultSummaryRequest.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def region_id(self):
        r"""Gets the region_id of this ShowVaultSummaryRequest.

        区域regionId

        :return: The region_id of this ShowVaultSummaryRequest.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this ShowVaultSummaryRequest.

        区域regionId

        :param region_id: The region_id of this ShowVaultSummaryRequest.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ShowVaultSummaryRequest.

        企业项目Id

        :return: The enterprise_project_id of this ShowVaultSummaryRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ShowVaultSummaryRequest.

        企业项目Id

        :param enterprise_project_id: The enterprise_project_id of this ShowVaultSummaryRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def start_time(self):
        r"""Gets the start_time of this ShowVaultSummaryRequest.

        开始时间,格式为“yyyy-mm-ddThh:mm:ssZ”

        :return: The start_time of this ShowVaultSummaryRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ShowVaultSummaryRequest.

        开始时间,格式为“yyyy-mm-ddThh:mm:ssZ”

        :param start_time: The start_time of this ShowVaultSummaryRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowVaultSummaryRequest.

        结束时间,格式为“yyyy-mm-ddThh:mm:ssZ”

        :return: The end_time of this ShowVaultSummaryRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowVaultSummaryRequest.

        结束时间,格式为“yyyy-mm-ddThh:mm:ssZ”

        :param end_time: The end_time of this ShowVaultSummaryRequest.
        :type end_time: str
        """
        self._end_time = end_time

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
        if not isinstance(other, ShowVaultSummaryRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
