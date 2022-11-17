# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRelationResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'case_relation_list': 'list[CaseRealtionInfo]'
    }

    attribute_map = {
        'case_relation_list': 'case_relation_list'
    }

    def __init__(self, case_relation_list=None):
        """ListRelationResponse

        The model defined in huaweicloud sdk

        :param case_relation_list: 关联工单列表
        :type case_relation_list: list[:class:`huaweicloudsdkosm.v2.CaseRealtionInfo`]
        """
        
        super(ListRelationResponse, self).__init__()

        self._case_relation_list = None
        self.discriminator = None

        if case_relation_list is not None:
            self.case_relation_list = case_relation_list

    @property
    def case_relation_list(self):
        """Gets the case_relation_list of this ListRelationResponse.

        关联工单列表

        :return: The case_relation_list of this ListRelationResponse.
        :rtype: list[:class:`huaweicloudsdkosm.v2.CaseRealtionInfo`]
        """
        return self._case_relation_list

    @case_relation_list.setter
    def case_relation_list(self, case_relation_list):
        """Sets the case_relation_list of this ListRelationResponse.

        关联工单列表

        :param case_relation_list: The case_relation_list of this ListRelationResponse.
        :type case_relation_list: list[:class:`huaweicloudsdkosm.v2.CaseRealtionInfo`]
        """
        self._case_relation_list = case_relation_list

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
        if not isinstance(other, ListRelationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
