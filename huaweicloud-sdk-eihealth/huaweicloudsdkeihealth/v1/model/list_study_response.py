# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListStudyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'studies': 'list[StudyRsp]'
    }

    attribute_map = {
        'count': 'count',
        'studies': 'studies'
    }

    def __init__(self, count=None, studies=None):
        """ListStudyResponse

        The model defined in huaweicloud sdk

        :param count: study总数
        :type count: int
        :param studies: study列表
        :type studies: list[:class:`huaweicloudsdkeihealth.v1.StudyRsp`]
        """
        
        super(ListStudyResponse, self).__init__()

        self._count = None
        self._studies = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if studies is not None:
            self.studies = studies

    @property
    def count(self):
        """Gets the count of this ListStudyResponse.

        study总数

        :return: The count of this ListStudyResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListStudyResponse.

        study总数

        :param count: The count of this ListStudyResponse.
        :type count: int
        """
        self._count = count

    @property
    def studies(self):
        """Gets the studies of this ListStudyResponse.

        study列表

        :return: The studies of this ListStudyResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.StudyRsp`]
        """
        return self._studies

    @studies.setter
    def studies(self, studies):
        """Sets the studies of this ListStudyResponse.

        study列表

        :param studies: The studies of this ListStudyResponse.
        :type studies: list[:class:`huaweicloudsdkeihealth.v1.StudyRsp`]
        """
        self._studies = studies

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
        if not isinstance(other, ListStudyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
