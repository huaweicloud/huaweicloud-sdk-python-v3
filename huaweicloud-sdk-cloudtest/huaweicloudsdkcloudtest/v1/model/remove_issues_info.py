# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RemoveIssuesInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workitem_list': 'list[WorkItemInfo]',
        'is_delete_case': 'bool'
    }

    attribute_map = {
        'workitem_list': 'workitem_list',
        'is_delete_case': 'is_delete_case'
    }

    def __init__(self, workitem_list=None, is_delete_case=None):
        r"""RemoveIssuesInfo

        The model defined in huaweicloud sdk

        :param workitem_list: 关联需求
        :type workitem_list: list[:class:`huaweicloudsdkcloudtest.v1.WorkItemInfo`]
        :param is_delete_case: 是否删除需求关联的用例
        :type is_delete_case: bool
        """
        
        

        self._workitem_list = None
        self._is_delete_case = None
        self.discriminator = None

        self.workitem_list = workitem_list
        if is_delete_case is not None:
            self.is_delete_case = is_delete_case

    @property
    def workitem_list(self):
        r"""Gets the workitem_list of this RemoveIssuesInfo.

        关联需求

        :return: The workitem_list of this RemoveIssuesInfo.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.WorkItemInfo`]
        """
        return self._workitem_list

    @workitem_list.setter
    def workitem_list(self, workitem_list):
        r"""Sets the workitem_list of this RemoveIssuesInfo.

        关联需求

        :param workitem_list: The workitem_list of this RemoveIssuesInfo.
        :type workitem_list: list[:class:`huaweicloudsdkcloudtest.v1.WorkItemInfo`]
        """
        self._workitem_list = workitem_list

    @property
    def is_delete_case(self):
        r"""Gets the is_delete_case of this RemoveIssuesInfo.

        是否删除需求关联的用例

        :return: The is_delete_case of this RemoveIssuesInfo.
        :rtype: bool
        """
        return self._is_delete_case

    @is_delete_case.setter
    def is_delete_case(self, is_delete_case):
        r"""Sets the is_delete_case of this RemoveIssuesInfo.

        是否删除需求关联的用例

        :param is_delete_case: The is_delete_case of this RemoveIssuesInfo.
        :type is_delete_case: bool
        """
        self._is_delete_case = is_delete_case

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
        if not isinstance(other, RemoveIssuesInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
