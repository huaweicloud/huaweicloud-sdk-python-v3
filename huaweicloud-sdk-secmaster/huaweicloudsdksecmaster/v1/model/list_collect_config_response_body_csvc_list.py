# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCollectConfigResponseBodyCsvcList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'csvc': 'str',
        'source_list': 'list[ListCollectConfigResponseBodySourceList]'
    }

    attribute_map = {
        'csvc': 'csvc',
        'source_list': 'source_list'
    }

    def __init__(self, csvc=None, source_list=None):
        r"""ListCollectConfigResponseBodyCsvcList

        The model defined in huaweicloud sdk

        :param csvc: 云产品ID
        :type csvc: str
        :param source_list: 所有的日志类型
        :type source_list: list[:class:`huaweicloudsdksecmaster.v1.ListCollectConfigResponseBodySourceList`]
        """
        
        

        self._csvc = None
        self._source_list = None
        self.discriminator = None

        if csvc is not None:
            self.csvc = csvc
        if source_list is not None:
            self.source_list = source_list

    @property
    def csvc(self):
        r"""Gets the csvc of this ListCollectConfigResponseBodyCsvcList.

        云产品ID

        :return: The csvc of this ListCollectConfigResponseBodyCsvcList.
        :rtype: str
        """
        return self._csvc

    @csvc.setter
    def csvc(self, csvc):
        r"""Sets the csvc of this ListCollectConfigResponseBodyCsvcList.

        云产品ID

        :param csvc: The csvc of this ListCollectConfigResponseBodyCsvcList.
        :type csvc: str
        """
        self._csvc = csvc

    @property
    def source_list(self):
        r"""Gets the source_list of this ListCollectConfigResponseBodyCsvcList.

        所有的日志类型

        :return: The source_list of this ListCollectConfigResponseBodyCsvcList.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.ListCollectConfigResponseBodySourceList`]
        """
        return self._source_list

    @source_list.setter
    def source_list(self, source_list):
        r"""Sets the source_list of this ListCollectConfigResponseBodyCsvcList.

        所有的日志类型

        :param source_list: The source_list of this ListCollectConfigResponseBodyCsvcList.
        :type source_list: list[:class:`huaweicloudsdksecmaster.v1.ListCollectConfigResponseBodySourceList`]
        """
        self._source_list = source_list

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
        if not isinstance(other, ListCollectConfigResponseBodyCsvcList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
