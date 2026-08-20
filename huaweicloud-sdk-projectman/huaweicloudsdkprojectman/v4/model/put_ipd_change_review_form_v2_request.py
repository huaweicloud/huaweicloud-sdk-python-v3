# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PutIpdChangeReviewFormV2Request:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'review_id': 'str',
        'body': 'ReviewUpdateBodyV2'
    }

    attribute_map = {
        'project_id': 'project_id',
        'review_id': 'review_id',
        'body': 'body'
    }

    def __init__(self, project_id=None, review_id=None, body=None):
        r"""PutIpdChangeReviewFormV2Request

        The model defined in huaweicloud sdk

        :param project_id: 项目32位ID，项目唯一标识。通过查询IPD项目列表获取，响应消息体中的id字段的值就是项目ID。
        :type project_id: str
        :param review_id: 评审单ID，评审单唯一标识。通过查询评审单列表（BR/GR）接口获取，响应消息体中的id字段的值就是评审单ID。
        :type review_id: str
        :param body: Body of the PutIpdChangeReviewFormV2Request
        :type body: :class:`huaweicloudsdkprojectman.v4.ReviewUpdateBodyV2`
        """
        
        

        self._project_id = None
        self._review_id = None
        self._body = None
        self.discriminator = None

        self.project_id = project_id
        self.review_id = review_id
        if body is not None:
            self.body = body

    @property
    def project_id(self):
        r"""Gets the project_id of this PutIpdChangeReviewFormV2Request.

        项目32位ID，项目唯一标识。通过查询IPD项目列表获取，响应消息体中的id字段的值就是项目ID。

        :return: The project_id of this PutIpdChangeReviewFormV2Request.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this PutIpdChangeReviewFormV2Request.

        项目32位ID，项目唯一标识。通过查询IPD项目列表获取，响应消息体中的id字段的值就是项目ID。

        :param project_id: The project_id of this PutIpdChangeReviewFormV2Request.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def review_id(self):
        r"""Gets the review_id of this PutIpdChangeReviewFormV2Request.

        评审单ID，评审单唯一标识。通过查询评审单列表（BR/GR）接口获取，响应消息体中的id字段的值就是评审单ID。

        :return: The review_id of this PutIpdChangeReviewFormV2Request.
        :rtype: str
        """
        return self._review_id

    @review_id.setter
    def review_id(self, review_id):
        r"""Sets the review_id of this PutIpdChangeReviewFormV2Request.

        评审单ID，评审单唯一标识。通过查询评审单列表（BR/GR）接口获取，响应消息体中的id字段的值就是评审单ID。

        :param review_id: The review_id of this PutIpdChangeReviewFormV2Request.
        :type review_id: str
        """
        self._review_id = review_id

    @property
    def body(self):
        r"""Gets the body of this PutIpdChangeReviewFormV2Request.

        :return: The body of this PutIpdChangeReviewFormV2Request.
        :rtype: :class:`huaweicloudsdkprojectman.v4.ReviewUpdateBodyV2`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this PutIpdChangeReviewFormV2Request.

        :param body: The body of this PutIpdChangeReviewFormV2Request.
        :type body: :class:`huaweicloudsdkprojectman.v4.ReviewUpdateBodyV2`
        """
        self._body = body

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
        if not isinstance(other, PutIpdChangeReviewFormV2Request):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
