# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowIpdThirdPartyAssociatedRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'issue_id': 'str',
        'project_id': 'str'
    }

    attribute_map = {
        'issue_id': 'issue_id',
        'project_id': 'project_id'
    }

    def __init__(self, issue_id=None, project_id=None):
        r"""ShowIpdThirdPartyAssociatedRequest

        The model defined in huaweicloud sdk

        :param issue_id: 工作项唯一ID。可以通过查询工作项列表或者查询树状工作项获取，响应消息体中的ID字段的值就是工作项ID。
        :type issue_id: str
        :param project_id: 项目32位ID，项目唯一标识，通过查询IPD项目列表获取，响应消息体中的project_id字段的值就是项目ID。
        :type project_id: str
        """
        
        

        self._issue_id = None
        self._project_id = None
        self.discriminator = None

        self.issue_id = issue_id
        self.project_id = project_id

    @property
    def issue_id(self):
        r"""Gets the issue_id of this ShowIpdThirdPartyAssociatedRequest.

        工作项唯一ID。可以通过查询工作项列表或者查询树状工作项获取，响应消息体中的ID字段的值就是工作项ID。

        :return: The issue_id of this ShowIpdThirdPartyAssociatedRequest.
        :rtype: str
        """
        return self._issue_id

    @issue_id.setter
    def issue_id(self, issue_id):
        r"""Sets the issue_id of this ShowIpdThirdPartyAssociatedRequest.

        工作项唯一ID。可以通过查询工作项列表或者查询树状工作项获取，响应消息体中的ID字段的值就是工作项ID。

        :param issue_id: The issue_id of this ShowIpdThirdPartyAssociatedRequest.
        :type issue_id: str
        """
        self._issue_id = issue_id

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowIpdThirdPartyAssociatedRequest.

        项目32位ID，项目唯一标识，通过查询IPD项目列表获取，响应消息体中的project_id字段的值就是项目ID。

        :return: The project_id of this ShowIpdThirdPartyAssociatedRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowIpdThirdPartyAssociatedRequest.

        项目32位ID，项目唯一标识，通过查询IPD项目列表获取，响应消息体中的project_id字段的值就是项目ID。

        :param project_id: The project_id of this ShowIpdThirdPartyAssociatedRequest.
        :type project_id: str
        """
        self._project_id = project_id

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowIpdThirdPartyAssociatedRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
