# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSubmissionsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'submissions': 'list[Submission]',
        'total': 'int',
        'page_no': 'int',
        'page_size': 'int'
    }

    attribute_map = {
        'submissions': 'submissions',
        'total': 'total',
        'page_no': 'page_no',
        'page_size': 'page_size'
    }

    def __init__(self, submissions=None, total=None, page_no=None, page_size=None):
        r"""ShowSubmissionsResponse

        The model defined in huaweicloud sdk

        :param submissions: 作业运行信息，详见submissions参数说明。
        :type submissions: list[:class:`huaweicloudsdkcdm.v1.Submission`]
        :param total: 查询该作业总的历史记录数。
        :type total: int
        :param page_no: 查询作业记录时，分页数。
        :type page_no: int
        :param page_size: 分页查询，每页返回的记录数。默认值：10。
        :type page_size: int
        """
        
        super(ShowSubmissionsResponse, self).__init__()

        self._submissions = None
        self._total = None
        self._page_no = None
        self._page_size = None
        self.discriminator = None

        if submissions is not None:
            self.submissions = submissions
        if total is not None:
            self.total = total
        if page_no is not None:
            self.page_no = page_no
        if page_size is not None:
            self.page_size = page_size

    @property
    def submissions(self):
        r"""Gets the submissions of this ShowSubmissionsResponse.

        作业运行信息，详见submissions参数说明。

        :return: The submissions of this ShowSubmissionsResponse.
        :rtype: list[:class:`huaweicloudsdkcdm.v1.Submission`]
        """
        return self._submissions

    @submissions.setter
    def submissions(self, submissions):
        r"""Sets the submissions of this ShowSubmissionsResponse.

        作业运行信息，详见submissions参数说明。

        :param submissions: The submissions of this ShowSubmissionsResponse.
        :type submissions: list[:class:`huaweicloudsdkcdm.v1.Submission`]
        """
        self._submissions = submissions

    @property
    def total(self):
        r"""Gets the total of this ShowSubmissionsResponse.

        查询该作业总的历史记录数。

        :return: The total of this ShowSubmissionsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ShowSubmissionsResponse.

        查询该作业总的历史记录数。

        :param total: The total of this ShowSubmissionsResponse.
        :type total: int
        """
        self._total = total

    @property
    def page_no(self):
        r"""Gets the page_no of this ShowSubmissionsResponse.

        查询作业记录时，分页数。

        :return: The page_no of this ShowSubmissionsResponse.
        :rtype: int
        """
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        r"""Sets the page_no of this ShowSubmissionsResponse.

        查询作业记录时，分页数。

        :param page_no: The page_no of this ShowSubmissionsResponse.
        :type page_no: int
        """
        self._page_no = page_no

    @property
    def page_size(self):
        r"""Gets the page_size of this ShowSubmissionsResponse.

        分页查询，每页返回的记录数。默认值：10。

        :return: The page_size of this ShowSubmissionsResponse.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this ShowSubmissionsResponse.

        分页查询，每页返回的记录数。默认值：10。

        :param page_size: The page_size of this ShowSubmissionsResponse.
        :type page_size: int
        """
        self._page_size = page_size

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
        if not isinstance(other, ShowSubmissionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
