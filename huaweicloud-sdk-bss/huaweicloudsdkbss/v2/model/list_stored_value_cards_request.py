# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListStoredValueCardsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'int',
        'card_id': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'status': 'status',
        'card_id': 'card_id',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, status=None, card_id=None, offset=None, limit=None):
        """ListStoredValueCardsRequest

        The model defined in huaweicloud sdk

        :param status: 状态：1：可使用2：已用完
        :type status: int
        :param card_id: 储值卡ID。此参数不携带或携带值为空时，不作为筛选条件。
        :type card_id: str
        :param offset: 偏移量，从0开始。默认值为0。 说明： offset用于分页处理，如不涉及分页，请使用默认值0。offset表示相对于满足条件的第一个数据的偏移量。如offset &#x3D; 1，则返回满足条件的第二个数据至最后一个数据。例如，满足查询条件的结果共10条数据，limit取值为10，offset取值为1，则返回的数据为2~10，第一条数据不返回。
        :type offset: int
        :param limit: 查询的优惠券数量，默认值为10。
        :type limit: int
        """
        
        

        self._status = None
        self._card_id = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.status = status
        if card_id is not None:
            self.card_id = card_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def status(self):
        """Gets the status of this ListStoredValueCardsRequest.

        状态：1：可使用2：已用完

        :return: The status of this ListStoredValueCardsRequest.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListStoredValueCardsRequest.

        状态：1：可使用2：已用完

        :param status: The status of this ListStoredValueCardsRequest.
        :type status: int
        """
        self._status = status

    @property
    def card_id(self):
        """Gets the card_id of this ListStoredValueCardsRequest.

        储值卡ID。此参数不携带或携带值为空时，不作为筛选条件。

        :return: The card_id of this ListStoredValueCardsRequest.
        :rtype: str
        """
        return self._card_id

    @card_id.setter
    def card_id(self, card_id):
        """Sets the card_id of this ListStoredValueCardsRequest.

        储值卡ID。此参数不携带或携带值为空时，不作为筛选条件。

        :param card_id: The card_id of this ListStoredValueCardsRequest.
        :type card_id: str
        """
        self._card_id = card_id

    @property
    def offset(self):
        """Gets the offset of this ListStoredValueCardsRequest.

        偏移量，从0开始。默认值为0。 说明： offset用于分页处理，如不涉及分页，请使用默认值0。offset表示相对于满足条件的第一个数据的偏移量。如offset = 1，则返回满足条件的第二个数据至最后一个数据。例如，满足查询条件的结果共10条数据，limit取值为10，offset取值为1，则返回的数据为2~10，第一条数据不返回。

        :return: The offset of this ListStoredValueCardsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListStoredValueCardsRequest.

        偏移量，从0开始。默认值为0。 说明： offset用于分页处理，如不涉及分页，请使用默认值0。offset表示相对于满足条件的第一个数据的偏移量。如offset = 1，则返回满足条件的第二个数据至最后一个数据。例如，满足查询条件的结果共10条数据，limit取值为10，offset取值为1，则返回的数据为2~10，第一条数据不返回。

        :param offset: The offset of this ListStoredValueCardsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListStoredValueCardsRequest.

        查询的优惠券数量，默认值为10。

        :return: The limit of this ListStoredValueCardsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListStoredValueCardsRequest.

        查询的优惠券数量，默认值为10。

        :param limit: The limit of this ListStoredValueCardsRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListStoredValueCardsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
