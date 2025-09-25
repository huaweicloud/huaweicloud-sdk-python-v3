# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowManualSecurityCheckStatusResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'scan_status': 'str',
        'total_host_num': 'int',
        'scaned_host_num': 'int',
        'content_num': 'int',
        'scan_progress': 'int'
    }

    attribute_map = {
        'scan_status': 'scan_status',
        'total_host_num': 'total_host_num',
        'scaned_host_num': 'scaned_host_num',
        'content_num': 'content_num',
        'scan_progress': 'scan_progress'
    }

    def __init__(self, scan_status=None, total_host_num=None, scaned_host_num=None, content_num=None, scan_progress=None):
        r"""ShowManualSecurityCheckStatusResponse

        The model defined in huaweicloud sdk

        :param scan_status: 体检状态
        :type scan_status: str
        :param total_host_num: 本次体检服务器数量
        :type total_host_num: int
        :param scaned_host_num: 体检完成的服务器数量
        :type scaned_host_num: int
        :param content_num: 体检内容数量
        :type content_num: int
        :param scan_progress: 体检进度百分比
        :type scan_progress: int
        """
        
        super(ShowManualSecurityCheckStatusResponse, self).__init__()

        self._scan_status = None
        self._total_host_num = None
        self._scaned_host_num = None
        self._content_num = None
        self._scan_progress = None
        self.discriminator = None

        if scan_status is not None:
            self.scan_status = scan_status
        if total_host_num is not None:
            self.total_host_num = total_host_num
        if scaned_host_num is not None:
            self.scaned_host_num = scaned_host_num
        if content_num is not None:
            self.content_num = content_num
        if scan_progress is not None:
            self.scan_progress = scan_progress

    @property
    def scan_status(self):
        r"""Gets the scan_status of this ShowManualSecurityCheckStatusResponse.

        体检状态

        :return: The scan_status of this ShowManualSecurityCheckStatusResponse.
        :rtype: str
        """
        return self._scan_status

    @scan_status.setter
    def scan_status(self, scan_status):
        r"""Sets the scan_status of this ShowManualSecurityCheckStatusResponse.

        体检状态

        :param scan_status: The scan_status of this ShowManualSecurityCheckStatusResponse.
        :type scan_status: str
        """
        self._scan_status = scan_status

    @property
    def total_host_num(self):
        r"""Gets the total_host_num of this ShowManualSecurityCheckStatusResponse.

        本次体检服务器数量

        :return: The total_host_num of this ShowManualSecurityCheckStatusResponse.
        :rtype: int
        """
        return self._total_host_num

    @total_host_num.setter
    def total_host_num(self, total_host_num):
        r"""Sets the total_host_num of this ShowManualSecurityCheckStatusResponse.

        本次体检服务器数量

        :param total_host_num: The total_host_num of this ShowManualSecurityCheckStatusResponse.
        :type total_host_num: int
        """
        self._total_host_num = total_host_num

    @property
    def scaned_host_num(self):
        r"""Gets the scaned_host_num of this ShowManualSecurityCheckStatusResponse.

        体检完成的服务器数量

        :return: The scaned_host_num of this ShowManualSecurityCheckStatusResponse.
        :rtype: int
        """
        return self._scaned_host_num

    @scaned_host_num.setter
    def scaned_host_num(self, scaned_host_num):
        r"""Sets the scaned_host_num of this ShowManualSecurityCheckStatusResponse.

        体检完成的服务器数量

        :param scaned_host_num: The scaned_host_num of this ShowManualSecurityCheckStatusResponse.
        :type scaned_host_num: int
        """
        self._scaned_host_num = scaned_host_num

    @property
    def content_num(self):
        r"""Gets the content_num of this ShowManualSecurityCheckStatusResponse.

        体检内容数量

        :return: The content_num of this ShowManualSecurityCheckStatusResponse.
        :rtype: int
        """
        return self._content_num

    @content_num.setter
    def content_num(self, content_num):
        r"""Sets the content_num of this ShowManualSecurityCheckStatusResponse.

        体检内容数量

        :param content_num: The content_num of this ShowManualSecurityCheckStatusResponse.
        :type content_num: int
        """
        self._content_num = content_num

    @property
    def scan_progress(self):
        r"""Gets the scan_progress of this ShowManualSecurityCheckStatusResponse.

        体检进度百分比

        :return: The scan_progress of this ShowManualSecurityCheckStatusResponse.
        :rtype: int
        """
        return self._scan_progress

    @scan_progress.setter
    def scan_progress(self, scan_progress):
        r"""Sets the scan_progress of this ShowManualSecurityCheckStatusResponse.

        体检进度百分比

        :param scan_progress: The scan_progress of this ShowManualSecurityCheckStatusResponse.
        :type scan_progress: int
        """
        self._scan_progress = scan_progress

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
        if not isinstance(other, ShowManualSecurityCheckStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
