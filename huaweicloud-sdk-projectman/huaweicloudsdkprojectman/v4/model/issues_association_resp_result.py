# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IssuesAssociationRespResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'fail': 'list[CreateThirdPartyAssociateDTO]',
        'success': 'list[CreateThirdPartyAssociateDTO]'
    }

    attribute_map = {
        'fail': 'fail',
        'success': 'success'
    }

    def __init__(self, fail=None, success=None):
        r"""IssuesAssociationRespResult

        The model defined in huaweicloud sdk

        :param fail: 关联失败的工作项列表。
        :type fail: list[:class:`huaweicloudsdkprojectman.v4.CreateThirdPartyAssociateDTO`]
        :param success: 关联成功的工作项列表。
        :type success: list[:class:`huaweicloudsdkprojectman.v4.CreateThirdPartyAssociateDTO`]
        """
        
        

        self._fail = None
        self._success = None
        self.discriminator = None

        if fail is not None:
            self.fail = fail
        if success is not None:
            self.success = success

    @property
    def fail(self):
        r"""Gets the fail of this IssuesAssociationRespResult.

        关联失败的工作项列表。

        :return: The fail of this IssuesAssociationRespResult.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.CreateThirdPartyAssociateDTO`]
        """
        return self._fail

    @fail.setter
    def fail(self, fail):
        r"""Sets the fail of this IssuesAssociationRespResult.

        关联失败的工作项列表。

        :param fail: The fail of this IssuesAssociationRespResult.
        :type fail: list[:class:`huaweicloudsdkprojectman.v4.CreateThirdPartyAssociateDTO`]
        """
        self._fail = fail

    @property
    def success(self):
        r"""Gets the success of this IssuesAssociationRespResult.

        关联成功的工作项列表。

        :return: The success of this IssuesAssociationRespResult.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.CreateThirdPartyAssociateDTO`]
        """
        return self._success

    @success.setter
    def success(self, success):
        r"""Sets the success of this IssuesAssociationRespResult.

        关联成功的工作项列表。

        :param success: The success of this IssuesAssociationRespResult.
        :type success: list[:class:`huaweicloudsdkprojectman.v4.CreateThirdPartyAssociateDTO`]
        """
        self._success = success

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
        if not isinstance(other, IssuesAssociationRespResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
