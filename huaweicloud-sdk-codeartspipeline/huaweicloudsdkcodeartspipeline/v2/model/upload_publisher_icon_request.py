# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UploadPublisherIconRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_id': 'str',
        'publisher_en_name': 'str',
        'body': 'UploadPublisherIconRequestBody'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'publisher_en_name': 'publisher_en_name',
        'body': 'body'
    }

    def __init__(self, domain_id=None, publisher_en_name=None, body=None):
        r"""UploadPublisherIconRequest

        The model defined in huaweicloud sdk

        :param domain_id: 租户ID
        :type domain_id: str
        :param publisher_en_name: 发布商名称
        :type publisher_en_name: str
        :param body: Body of the UploadPublisherIconRequest
        :type body: :class:`huaweicloudsdkcodeartspipeline.v2.UploadPublisherIconRequestBody`
        """
        
        

        self._domain_id = None
        self._publisher_en_name = None
        self._body = None
        self.discriminator = None

        self.domain_id = domain_id
        self.publisher_en_name = publisher_en_name
        if body is not None:
            self.body = body

    @property
    def domain_id(self):
        r"""Gets the domain_id of this UploadPublisherIconRequest.

        租户ID

        :return: The domain_id of this UploadPublisherIconRequest.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this UploadPublisherIconRequest.

        租户ID

        :param domain_id: The domain_id of this UploadPublisherIconRequest.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def publisher_en_name(self):
        r"""Gets the publisher_en_name of this UploadPublisherIconRequest.

        发布商名称

        :return: The publisher_en_name of this UploadPublisherIconRequest.
        :rtype: str
        """
        return self._publisher_en_name

    @publisher_en_name.setter
    def publisher_en_name(self, publisher_en_name):
        r"""Sets the publisher_en_name of this UploadPublisherIconRequest.

        发布商名称

        :param publisher_en_name: The publisher_en_name of this UploadPublisherIconRequest.
        :type publisher_en_name: str
        """
        self._publisher_en_name = publisher_en_name

    @property
    def body(self):
        r"""Gets the body of this UploadPublisherIconRequest.

        :return: The body of this UploadPublisherIconRequest.
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.UploadPublisherIconRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UploadPublisherIconRequest.

        :param body: The body of this UploadPublisherIconRequest.
        :type body: :class:`huaweicloudsdkcodeartspipeline.v2.UploadPublisherIconRequestBody`
        """
        self._body = body

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
        if not isinstance(other, UploadPublisherIconRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
