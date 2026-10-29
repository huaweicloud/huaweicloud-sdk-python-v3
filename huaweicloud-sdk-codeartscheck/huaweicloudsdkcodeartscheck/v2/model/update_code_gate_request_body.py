# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateCodeGateRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'review_data': 'list[ReviewDataInfoRequestParam]',
        'id': 'str'
    }

    attribute_map = {
        'review_data': 'reviewData',
        'id': 'id'
    }

    def __init__(self, review_data=None, id=None):
        r"""UpdateCodeGateRequestBody

        The model defined in huaweicloud sdk

        :param review_data: **参数解释：** 任务门禁配置列表。 **约束限制：** 不涉及。
        :type review_data: list[:class:`huaweicloudsdkcodeartscheck.v2.ReviewDataInfoRequestParam`]
        :param id: **参数解释：** 任务ID，即新建检查任务接口的返回值，每个代码检查任务及其下的分支任务、通过API创建的增量任务都有唯一的任务ID。即[[查询任务列表](https://support.huaweicloud.com/api-codecheck/ShowTasksList.html)](tag:hws)[[查询任务列表](https://support.huaweicloud.com/intl/zh-cn/api-codecheck/ShowTasksList.html)](tag:hws_hk)[查询任务列表](tag:hcs,hcs_sm)接口响应中的id字段。 **约束限制：** 不涉及。 **取值范围：** 长度为[1~32]个字符。 **默认取值：** 不涉及。
        :type id: str
        """
        
        

        self._review_data = None
        self._id = None
        self.discriminator = None

        self.review_data = review_data
        self.id = id

    @property
    def review_data(self):
        r"""Gets the review_data of this UpdateCodeGateRequestBody.

        **参数解释：** 任务门禁配置列表。 **约束限制：** 不涉及。

        :return: The review_data of this UpdateCodeGateRequestBody.
        :rtype: list[:class:`huaweicloudsdkcodeartscheck.v2.ReviewDataInfoRequestParam`]
        """
        return self._review_data

    @review_data.setter
    def review_data(self, review_data):
        r"""Sets the review_data of this UpdateCodeGateRequestBody.

        **参数解释：** 任务门禁配置列表。 **约束限制：** 不涉及。

        :param review_data: The review_data of this UpdateCodeGateRequestBody.
        :type review_data: list[:class:`huaweicloudsdkcodeartscheck.v2.ReviewDataInfoRequestParam`]
        """
        self._review_data = review_data

    @property
    def id(self):
        r"""Gets the id of this UpdateCodeGateRequestBody.

        **参数解释：** 任务ID，即新建检查任务接口的返回值，每个代码检查任务及其下的分支任务、通过API创建的增量任务都有唯一的任务ID。即[[查询任务列表](https://support.huaweicloud.com/api-codecheck/ShowTasksList.html)](tag:hws)[[查询任务列表](https://support.huaweicloud.com/intl/zh-cn/api-codecheck/ShowTasksList.html)](tag:hws_hk)[查询任务列表](tag:hcs,hcs_sm)接口响应中的id字段。 **约束限制：** 不涉及。 **取值范围：** 长度为[1~32]个字符。 **默认取值：** 不涉及。

        :return: The id of this UpdateCodeGateRequestBody.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UpdateCodeGateRequestBody.

        **参数解释：** 任务ID，即新建检查任务接口的返回值，每个代码检查任务及其下的分支任务、通过API创建的增量任务都有唯一的任务ID。即[[查询任务列表](https://support.huaweicloud.com/api-codecheck/ShowTasksList.html)](tag:hws)[[查询任务列表](https://support.huaweicloud.com/intl/zh-cn/api-codecheck/ShowTasksList.html)](tag:hws_hk)[查询任务列表](tag:hcs,hcs_sm)接口响应中的id字段。 **约束限制：** 不涉及。 **取值范围：** 长度为[1~32]个字符。 **默认取值：** 不涉及。

        :param id: The id of this UpdateCodeGateRequestBody.
        :type id: str
        """
        self._id = id

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
        if not isinstance(other, UpdateCodeGateRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
