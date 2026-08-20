# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ThirdPartyAssociatedResultData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'result': 'list[ThirdPartyAssociatedDTO]',
        'page': 'PageVO'
    }

    attribute_map = {
        'result': 'result',
        'page': 'page'
    }

    def __init__(self, result=None, page=None):
        r"""ThirdPartyAssociatedResultData

        The model defined in huaweicloud sdk

        :param result: 工作项关联外部链接查询结果数据集合
        :type result: list[:class:`huaweicloudsdkprojectman.v4.ThirdPartyAssociatedDTO`]
        :param page: 
        :type page: :class:`huaweicloudsdkprojectman.v4.PageVO`
        """
        
        

        self._result = None
        self._page = None
        self.discriminator = None

        if result is not None:
            self.result = result
        if page is not None:
            self.page = page

    @property
    def result(self):
        r"""Gets the result of this ThirdPartyAssociatedResultData.

        工作项关联外部链接查询结果数据集合

        :return: The result of this ThirdPartyAssociatedResultData.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.ThirdPartyAssociatedDTO`]
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this ThirdPartyAssociatedResultData.

        工作项关联外部链接查询结果数据集合

        :param result: The result of this ThirdPartyAssociatedResultData.
        :type result: list[:class:`huaweicloudsdkprojectman.v4.ThirdPartyAssociatedDTO`]
        """
        self._result = result

    @property
    def page(self):
        r"""Gets the page of this ThirdPartyAssociatedResultData.

        :return: The page of this ThirdPartyAssociatedResultData.
        :rtype: :class:`huaweicloudsdkprojectman.v4.PageVO`
        """
        return self._page

    @page.setter
    def page(self, page):
        r"""Sets the page of this ThirdPartyAssociatedResultData.

        :param page: The page of this ThirdPartyAssociatedResultData.
        :type page: :class:`huaweicloudsdkprojectman.v4.PageVO`
        """
        self._page = page

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
        if not isinstance(other, ThirdPartyAssociatedResultData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
