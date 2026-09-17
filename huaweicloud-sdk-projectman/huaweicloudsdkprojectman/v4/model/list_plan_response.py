# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPlanResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'message': 'str',
        'result': 'list[PlanResponseResult]',
        'page': 'PlanListResponsePage'
    }

    attribute_map = {
        'status': 'status',
        'message': 'message',
        'result': 'result',
        'page': 'page'
    }

    def __init__(self, status=None, message=None, result=None, page=None):
        r"""ListPlanResponse

        The model defined in huaweicloud sdk

        :param status: **参数解释**： 返回状态。 **取值范围**： - success：查询计划列表成功 - error：查询计划列表失败
        :type status: str
        :param message: **参数解释**： 提示信息。 **取值范围**： 不涉及。
        :type message: str
        :param result: **参数解释**： 计划列表，包含发布及其子迭代的完整信息。
        :type result: list[:class:`huaweicloudsdkprojectman.v4.PlanResponseResult`]
        :param page: 
        :type page: :class:`huaweicloudsdkprojectman.v4.PlanListResponsePage`
        """
        
        super().__init__()

        self._status = None
        self._message = None
        self._result = None
        self._page = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if message is not None:
            self.message = message
        if result is not None:
            self.result = result
        if page is not None:
            self.page = page

    @property
    def status(self):
        r"""Gets the status of this ListPlanResponse.

        **参数解释**： 返回状态。 **取值范围**： - success：查询计划列表成功 - error：查询计划列表失败

        :return: The status of this ListPlanResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListPlanResponse.

        **参数解释**： 返回状态。 **取值范围**： - success：查询计划列表成功 - error：查询计划列表失败

        :param status: The status of this ListPlanResponse.
        :type status: str
        """
        self._status = status

    @property
    def message(self):
        r"""Gets the message of this ListPlanResponse.

        **参数解释**： 提示信息。 **取值范围**： 不涉及。

        :return: The message of this ListPlanResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this ListPlanResponse.

        **参数解释**： 提示信息。 **取值范围**： 不涉及。

        :param message: The message of this ListPlanResponse.
        :type message: str
        """
        self._message = message

    @property
    def result(self):
        r"""Gets the result of this ListPlanResponse.

        **参数解释**： 计划列表，包含发布及其子迭代的完整信息。

        :return: The result of this ListPlanResponse.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.PlanResponseResult`]
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this ListPlanResponse.

        **参数解释**： 计划列表，包含发布及其子迭代的完整信息。

        :param result: The result of this ListPlanResponse.
        :type result: list[:class:`huaweicloudsdkprojectman.v4.PlanResponseResult`]
        """
        self._result = result

    @property
    def page(self):
        r"""Gets the page of this ListPlanResponse.

        :return: The page of this ListPlanResponse.
        :rtype: :class:`huaweicloudsdkprojectman.v4.PlanListResponsePage`
        """
        return self._page

    @page.setter
    def page(self, page):
        r"""Sets the page of this ListPlanResponse.

        :param page: The page of this ListPlanResponse.
        :type page: :class:`huaweicloudsdkprojectman.v4.PlanListResponsePage`
        """
        self._page = page

    def to_dict(self):
        import warnings
        warnings.warn("ListPlanResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ListPlanResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
