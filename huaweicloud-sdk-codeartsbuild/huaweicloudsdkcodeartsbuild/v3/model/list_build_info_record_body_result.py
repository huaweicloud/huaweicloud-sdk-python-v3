# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBuildInfoRecordBodyResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'health_score': 'str',
        'page_index': 'str',
        'total_page': 'str',
        'total_record': 'str',
        'job_build_states': 'list[BuildInfoRecord]'
    }

    attribute_map = {
        'health_score': 'health_score',
        'page_index': 'page_index',
        'total_page': 'total_page',
        'total_record': 'total_record',
        'job_build_states': 'job_build_states'
    }

    def __init__(self, health_score=None, page_index=None, total_page=None, total_record=None, job_build_states=None):
        r"""ListBuildInfoRecordBodyResult

        The model defined in huaweicloud sdk

        :param health_score: 健康度
        :type health_score: str
        :param page_index: 分页页数
        :type page_index: str
        :param total_page: 总页数
        :type total_page: str
        :param total_record: 总条数
        :type total_record: str
        :param job_build_states: 构建历史详情列表
        :type job_build_states: list[:class:`huaweicloudsdkcodeartsbuild.v3.BuildInfoRecord`]
        """
        
        

        self._health_score = None
        self._page_index = None
        self._total_page = None
        self._total_record = None
        self._job_build_states = None
        self.discriminator = None

        if health_score is not None:
            self.health_score = health_score
        if page_index is not None:
            self.page_index = page_index
        if total_page is not None:
            self.total_page = total_page
        if total_record is not None:
            self.total_record = total_record
        if job_build_states is not None:
            self.job_build_states = job_build_states

    @property
    def health_score(self):
        r"""Gets the health_score of this ListBuildInfoRecordBodyResult.

        健康度

        :return: The health_score of this ListBuildInfoRecordBodyResult.
        :rtype: str
        """
        return self._health_score

    @health_score.setter
    def health_score(self, health_score):
        r"""Sets the health_score of this ListBuildInfoRecordBodyResult.

        健康度

        :param health_score: The health_score of this ListBuildInfoRecordBodyResult.
        :type health_score: str
        """
        self._health_score = health_score

    @property
    def page_index(self):
        r"""Gets the page_index of this ListBuildInfoRecordBodyResult.

        分页页数

        :return: The page_index of this ListBuildInfoRecordBodyResult.
        :rtype: str
        """
        return self._page_index

    @page_index.setter
    def page_index(self, page_index):
        r"""Sets the page_index of this ListBuildInfoRecordBodyResult.

        分页页数

        :param page_index: The page_index of this ListBuildInfoRecordBodyResult.
        :type page_index: str
        """
        self._page_index = page_index

    @property
    def total_page(self):
        r"""Gets the total_page of this ListBuildInfoRecordBodyResult.

        总页数

        :return: The total_page of this ListBuildInfoRecordBodyResult.
        :rtype: str
        """
        return self._total_page

    @total_page.setter
    def total_page(self, total_page):
        r"""Sets the total_page of this ListBuildInfoRecordBodyResult.

        总页数

        :param total_page: The total_page of this ListBuildInfoRecordBodyResult.
        :type total_page: str
        """
        self._total_page = total_page

    @property
    def total_record(self):
        r"""Gets the total_record of this ListBuildInfoRecordBodyResult.

        总条数

        :return: The total_record of this ListBuildInfoRecordBodyResult.
        :rtype: str
        """
        return self._total_record

    @total_record.setter
    def total_record(self, total_record):
        r"""Sets the total_record of this ListBuildInfoRecordBodyResult.

        总条数

        :param total_record: The total_record of this ListBuildInfoRecordBodyResult.
        :type total_record: str
        """
        self._total_record = total_record

    @property
    def job_build_states(self):
        r"""Gets the job_build_states of this ListBuildInfoRecordBodyResult.

        构建历史详情列表

        :return: The job_build_states of this ListBuildInfoRecordBodyResult.
        :rtype: list[:class:`huaweicloudsdkcodeartsbuild.v3.BuildInfoRecord`]
        """
        return self._job_build_states

    @job_build_states.setter
    def job_build_states(self, job_build_states):
        r"""Sets the job_build_states of this ListBuildInfoRecordBodyResult.

        构建历史详情列表

        :param job_build_states: The job_build_states of this ListBuildInfoRecordBodyResult.
        :type job_build_states: list[:class:`huaweicloudsdkcodeartsbuild.v3.BuildInfoRecord`]
        """
        self._job_build_states = job_build_states

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
        if not isinstance(other, ListBuildInfoRecordBodyResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
