# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StartJobResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'submissions': 'list[StartJobSubmission]'
    }

    attribute_map = {
        'submissions': 'submissions'
    }

    def __init__(self, submissions=None):
        """StartJobResponse

        The model defined in huaweicloud sdk

        :param submissions: 作业运行信息，请参见submission参数说明
        :type submissions: list[:class:`huaweicloudsdkcdm.v1.StartJobSubmission`]
        """
        
        super(StartJobResponse, self).__init__()

        self._submissions = None
        self.discriminator = None

        if submissions is not None:
            self.submissions = submissions

    @property
    def submissions(self):
        """Gets the submissions of this StartJobResponse.

        作业运行信息，请参见submission参数说明

        :return: The submissions of this StartJobResponse.
        :rtype: list[:class:`huaweicloudsdkcdm.v1.StartJobSubmission`]
        """
        return self._submissions

    @submissions.setter
    def submissions(self, submissions):
        """Sets the submissions of this StartJobResponse.

        作业运行信息，请参见submission参数说明

        :param submissions: The submissions of this StartJobResponse.
        :type submissions: list[:class:`huaweicloudsdkcdm.v1.StartJobSubmission`]
        """
        self._submissions = submissions

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
        if not isinstance(other, StartJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
