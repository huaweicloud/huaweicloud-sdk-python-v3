# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRelationBucketsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'assets_name': 'str',
        'risk_start': 'int',
        'risk_end': 'int',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'job_id': 'job_id',
        'assets_name': 'assets_name',
        'risk_start': 'risk_start',
        'risk_end': 'risk_end',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, job_id=None, assets_name=None, risk_start=None, risk_end=None, offset=None, limit=None):
        """ListRelationBucketsRequest

        The model defined in huaweicloud sdk

        :param job_id: 任务ID
        :type job_id: str
        :param assets_name: 资产名称
        :type assets_name: str
        :param risk_start: 起始风险等级
        :type risk_start: int
        :param risk_end: 终止风险等级
        :type risk_end: int
        :param offset: 页码
        :type offset: int
        :param limit: 分页大小
        :type limit: int
        """
        
        

        self._job_id = None
        self._assets_name = None
        self._risk_start = None
        self._risk_end = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.job_id = job_id
        if assets_name is not None:
            self.assets_name = assets_name
        self.risk_start = risk_start
        self.risk_end = risk_end
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def job_id(self):
        """Gets the job_id of this ListRelationBucketsRequest.

        任务ID

        :return: The job_id of this ListRelationBucketsRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ListRelationBucketsRequest.

        任务ID

        :param job_id: The job_id of this ListRelationBucketsRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def assets_name(self):
        """Gets the assets_name of this ListRelationBucketsRequest.

        资产名称

        :return: The assets_name of this ListRelationBucketsRequest.
        :rtype: str
        """
        return self._assets_name

    @assets_name.setter
    def assets_name(self, assets_name):
        """Sets the assets_name of this ListRelationBucketsRequest.

        资产名称

        :param assets_name: The assets_name of this ListRelationBucketsRequest.
        :type assets_name: str
        """
        self._assets_name = assets_name

    @property
    def risk_start(self):
        """Gets the risk_start of this ListRelationBucketsRequest.

        起始风险等级

        :return: The risk_start of this ListRelationBucketsRequest.
        :rtype: int
        """
        return self._risk_start

    @risk_start.setter
    def risk_start(self, risk_start):
        """Sets the risk_start of this ListRelationBucketsRequest.

        起始风险等级

        :param risk_start: The risk_start of this ListRelationBucketsRequest.
        :type risk_start: int
        """
        self._risk_start = risk_start

    @property
    def risk_end(self):
        """Gets the risk_end of this ListRelationBucketsRequest.

        终止风险等级

        :return: The risk_end of this ListRelationBucketsRequest.
        :rtype: int
        """
        return self._risk_end

    @risk_end.setter
    def risk_end(self, risk_end):
        """Sets the risk_end of this ListRelationBucketsRequest.

        终止风险等级

        :param risk_end: The risk_end of this ListRelationBucketsRequest.
        :type risk_end: int
        """
        self._risk_end = risk_end

    @property
    def offset(self):
        """Gets the offset of this ListRelationBucketsRequest.

        页码

        :return: The offset of this ListRelationBucketsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListRelationBucketsRequest.

        页码

        :param offset: The offset of this ListRelationBucketsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListRelationBucketsRequest.

        分页大小

        :return: The limit of this ListRelationBucketsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListRelationBucketsRequest.

        分页大小

        :param limit: The limit of this ListRelationBucketsRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListRelationBucketsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
