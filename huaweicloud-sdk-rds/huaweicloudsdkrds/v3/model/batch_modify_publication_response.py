# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchModifyPublicationResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'publications': 'list[BatchOperateResponseInfo]'
    }

    attribute_map = {
        'publications': 'publications'
    }

    def __init__(self, publications=None):
        r"""BatchModifyPublicationResponse

        The model defined in huaweicloud sdk

        :param publications: 修改发布结果。
        :type publications: list[:class:`huaweicloudsdkrds.v3.BatchOperateResponseInfo`]
        """
        
        super().__init__()

        self._publications = None
        self.discriminator = None

        if publications is not None:
            self.publications = publications

    @property
    def publications(self):
        r"""Gets the publications of this BatchModifyPublicationResponse.

        修改发布结果。

        :return: The publications of this BatchModifyPublicationResponse.
        :rtype: list[:class:`huaweicloudsdkrds.v3.BatchOperateResponseInfo`]
        """
        return self._publications

    @publications.setter
    def publications(self, publications):
        r"""Sets the publications of this BatchModifyPublicationResponse.

        修改发布结果。

        :param publications: The publications of this BatchModifyPublicationResponse.
        :type publications: list[:class:`huaweicloudsdkrds.v3.BatchOperateResponseInfo`]
        """
        self._publications = publications

    def to_dict(self):
        import warnings
        warnings.warn("BatchModifyPublicationResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, BatchModifyPublicationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
