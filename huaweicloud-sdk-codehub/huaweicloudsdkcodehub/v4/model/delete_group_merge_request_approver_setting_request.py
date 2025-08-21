# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteGroupMergeRequestApproverSettingRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_id': 'int',
        'setting_id': 'int'
    }

    attribute_map = {
        'group_id': 'group_id',
        'setting_id': 'setting_id'
    }

    def __init__(self, group_id=None, setting_id=None):
        r"""DeleteGroupMergeRequestApproverSettingRequest

        The model defined in huaweicloud sdk

        :param group_id: **参数解释：** 代码组id，代码组首页，Group ID后的数字Id
        :type group_id: int
        :param setting_id: **参数解释：** 合并请求审核设置id。
        :type setting_id: int
        """
        
        

        self._group_id = None
        self._setting_id = None
        self.discriminator = None

        self.group_id = group_id
        self.setting_id = setting_id

    @property
    def group_id(self):
        r"""Gets the group_id of this DeleteGroupMergeRequestApproverSettingRequest.

        **参数解释：** 代码组id，代码组首页，Group ID后的数字Id

        :return: The group_id of this DeleteGroupMergeRequestApproverSettingRequest.
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this DeleteGroupMergeRequestApproverSettingRequest.

        **参数解释：** 代码组id，代码组首页，Group ID后的数字Id

        :param group_id: The group_id of this DeleteGroupMergeRequestApproverSettingRequest.
        :type group_id: int
        """
        self._group_id = group_id

    @property
    def setting_id(self):
        r"""Gets the setting_id of this DeleteGroupMergeRequestApproverSettingRequest.

        **参数解释：** 合并请求审核设置id。

        :return: The setting_id of this DeleteGroupMergeRequestApproverSettingRequest.
        :rtype: int
        """
        return self._setting_id

    @setting_id.setter
    def setting_id(self, setting_id):
        r"""Sets the setting_id of this DeleteGroupMergeRequestApproverSettingRequest.

        **参数解释：** 合并请求审核设置id。

        :param setting_id: The setting_id of this DeleteGroupMergeRequestApproverSettingRequest.
        :type setting_id: int
        """
        self._setting_id = setting_id

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
        if not isinstance(other, DeleteGroupMergeRequestApproverSettingRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
