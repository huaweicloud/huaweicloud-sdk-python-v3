# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFacialAnimationsDataResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'csv_file_download_url': 'str',
        'state': 'str',
        'error_message': 'str'
    }

    attribute_map = {
        'csv_file_download_url': 'csv_file_download_url',
        'state': 'state',
        'error_message': 'error_message'
    }

    def __init__(self, csv_file_download_url=None, state=None, error_message=None):
        r"""ListFacialAnimationsDataResponse

        The model defined in huaweicloud sdk

        :param csv_file_download_url: csv文件下载地址
        :type csv_file_download_url: str
        :param state: 任务的状态。 * PROCESSING：处理中 * SUCCEED：成功 * FAILED：失败
        :type state: str
        :param error_message: 失败任务描述
        :type error_message: str
        """
        
        super(ListFacialAnimationsDataResponse, self).__init__()

        self._csv_file_download_url = None
        self._state = None
        self._error_message = None
        self.discriminator = None

        if csv_file_download_url is not None:
            self.csv_file_download_url = csv_file_download_url
        if state is not None:
            self.state = state
        if error_message is not None:
            self.error_message = error_message

    @property
    def csv_file_download_url(self):
        r"""Gets the csv_file_download_url of this ListFacialAnimationsDataResponse.

        csv文件下载地址

        :return: The csv_file_download_url of this ListFacialAnimationsDataResponse.
        :rtype: str
        """
        return self._csv_file_download_url

    @csv_file_download_url.setter
    def csv_file_download_url(self, csv_file_download_url):
        r"""Sets the csv_file_download_url of this ListFacialAnimationsDataResponse.

        csv文件下载地址

        :param csv_file_download_url: The csv_file_download_url of this ListFacialAnimationsDataResponse.
        :type csv_file_download_url: str
        """
        self._csv_file_download_url = csv_file_download_url

    @property
    def state(self):
        r"""Gets the state of this ListFacialAnimationsDataResponse.

        任务的状态。 * PROCESSING：处理中 * SUCCEED：成功 * FAILED：失败

        :return: The state of this ListFacialAnimationsDataResponse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this ListFacialAnimationsDataResponse.

        任务的状态。 * PROCESSING：处理中 * SUCCEED：成功 * FAILED：失败

        :param state: The state of this ListFacialAnimationsDataResponse.
        :type state: str
        """
        self._state = state

    @property
    def error_message(self):
        r"""Gets the error_message of this ListFacialAnimationsDataResponse.

        失败任务描述

        :return: The error_message of this ListFacialAnimationsDataResponse.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        r"""Sets the error_message of this ListFacialAnimationsDataResponse.

        失败任务描述

        :param error_message: The error_message of this ListFacialAnimationsDataResponse.
        :type error_message: str
        """
        self._error_message = error_message

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
        if not isinstance(other, ListFacialAnimationsDataResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
