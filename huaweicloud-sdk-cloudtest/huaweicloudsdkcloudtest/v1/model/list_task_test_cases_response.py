# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTaskTestCasesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'related_case_uris': 'list[str]',
        'not_related_case_uris': 'list[str]',
        'case_task_info': 'list[RelateTaskTestCasesVo]'
    }

    attribute_map = {
        'related_case_uris': 'related_case_uris',
        'not_related_case_uris': 'not_related_case_uris',
        'case_task_info': 'case_task_info'
    }

    def __init__(self, related_case_uris=None, not_related_case_uris=None, case_task_info=None):
        """ListTaskTestCasesResponse

        The model defined in huaweicloud sdk

        :param related_case_uris: 关联的用例uris
        :type related_case_uris: list[str]
        :param not_related_case_uris: 未关联的用例uris
        :type not_related_case_uris: list[str]
        :param case_task_info: 用例及任务信息
        :type case_task_info: list[:class:`huaweicloudsdkcloudtest.v1.RelateTaskTestCasesVo`]
        """
        
        super(ListTaskTestCasesResponse, self).__init__()

        self._related_case_uris = None
        self._not_related_case_uris = None
        self._case_task_info = None
        self.discriminator = None

        if related_case_uris is not None:
            self.related_case_uris = related_case_uris
        if not_related_case_uris is not None:
            self.not_related_case_uris = not_related_case_uris
        if case_task_info is not None:
            self.case_task_info = case_task_info

    @property
    def related_case_uris(self):
        """Gets the related_case_uris of this ListTaskTestCasesResponse.

        关联的用例uris

        :return: The related_case_uris of this ListTaskTestCasesResponse.
        :rtype: list[str]
        """
        return self._related_case_uris

    @related_case_uris.setter
    def related_case_uris(self, related_case_uris):
        """Sets the related_case_uris of this ListTaskTestCasesResponse.

        关联的用例uris

        :param related_case_uris: The related_case_uris of this ListTaskTestCasesResponse.
        :type related_case_uris: list[str]
        """
        self._related_case_uris = related_case_uris

    @property
    def not_related_case_uris(self):
        """Gets the not_related_case_uris of this ListTaskTestCasesResponse.

        未关联的用例uris

        :return: The not_related_case_uris of this ListTaskTestCasesResponse.
        :rtype: list[str]
        """
        return self._not_related_case_uris

    @not_related_case_uris.setter
    def not_related_case_uris(self, not_related_case_uris):
        """Sets the not_related_case_uris of this ListTaskTestCasesResponse.

        未关联的用例uris

        :param not_related_case_uris: The not_related_case_uris of this ListTaskTestCasesResponse.
        :type not_related_case_uris: list[str]
        """
        self._not_related_case_uris = not_related_case_uris

    @property
    def case_task_info(self):
        """Gets the case_task_info of this ListTaskTestCasesResponse.

        用例及任务信息

        :return: The case_task_info of this ListTaskTestCasesResponse.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.RelateTaskTestCasesVo`]
        """
        return self._case_task_info

    @case_task_info.setter
    def case_task_info(self, case_task_info):
        """Sets the case_task_info of this ListTaskTestCasesResponse.

        用例及任务信息

        :param case_task_info: The case_task_info of this ListTaskTestCasesResponse.
        :type case_task_info: list[:class:`huaweicloudsdkcloudtest.v1.RelateTaskTestCasesVo`]
        """
        self._case_task_info = case_task_info

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
        if not isinstance(other, ListTaskTestCasesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
