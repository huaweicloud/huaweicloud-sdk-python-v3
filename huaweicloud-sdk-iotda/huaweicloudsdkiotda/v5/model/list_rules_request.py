# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRulesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'app_id': 'str',
        'rule_type': 'str',
        'limit': 'int',
        'marker': 'str',
        'offset': 'int'
    }

    attribute_map = {
        'instance_id': 'Instance-Id',
        'app_id': 'app_id',
        'rule_type': 'rule_type',
        'limit': 'limit',
        'marker': 'marker',
        'offset': 'offset'
    }

    def __init__(self, instance_id=None, app_id=None, rule_type=None, limit=None, marker=None, offset=None):
        """ListRulesRequest

        The model defined in huaweicloud sdk

        :param instance_id: **参数说明**：实例ID。物理多租下各实例的唯一标识，一般华为云租户无需携带该参数，仅在物理多租场景下从管理面访问API时需要携带该参数。
        :type instance_id: str
        :param app_id: **参数说明**：资源空间ID。此参数为非必选参数，存在多资源空间的用户需要使用该接口时，可以携带该参数查询指定资源空间下的规则列表，不携带该参数则会查询该用户下所有规则列表。 **取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。
        :type app_id: str
        :param rule_type: **参数说明**：规则类型。此参数为非必选参数，指定对应的规则类型结果进行返回，不携带该参数则会返回所有类型规则。 **取值范围**： - DEVICE_LINKAGE - DATA_FORWARDING
        :type rule_type: str
        :param limit: **参数说明**：分页查询时每页显示的记录数，查询结果根据limit进行分页。 **取值范围**：1-50的整数，默认值为10。
        :type limit: int
        :param marker: **参数说明**：上一次分页查询结果中最后一条记录的ID，在上一次分页查询时由物联网平台返回获得。分页查询时物联网平台是按marker也就是记录ID降序查询的，越新的数据记录ID也会越大。若填写marker，则本次只查询记录ID小于marker的数据记录。若不填写，则从记录ID最大也就是最新的一条数据开始查询。如果需要依次查询所有数据，则每次查询时必须填写上一次查询响应中的marker值。 **取值范围**：长度为24的十六进制字符串，默认值为ffffffffffffffffffffffff。
        :type marker: str
        :param offset: **参数说明**：表示从marker后偏移offset条记录开始查询。默认为0，取值范围为0-500的整数。当offset为0时，表示从marker后第一条记录开始输出。限制offset最大值是出于API性能考虑，您可以搭配marker使用该参数实现翻页，例如每页50条记录，1-11页内都可以直接使用offset跳转到指定页，但到11页后，由于offset限制为500，您需要使用第11页返回的marker作为下次查询的marker，以实现翻页到12-22页。 **取值范围**：0-500的整数，默认为0。
        :type offset: int
        """
        
        

        self._instance_id = None
        self._app_id = None
        self._rule_type = None
        self._limit = None
        self._marker = None
        self._offset = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if app_id is not None:
            self.app_id = app_id
        if rule_type is not None:
            self.rule_type = rule_type
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if offset is not None:
            self.offset = offset

    @property
    def instance_id(self):
        """Gets the instance_id of this ListRulesRequest.

        **参数说明**：实例ID。物理多租下各实例的唯一标识，一般华为云租户无需携带该参数，仅在物理多租场景下从管理面访问API时需要携带该参数。

        :return: The instance_id of this ListRulesRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListRulesRequest.

        **参数说明**：实例ID。物理多租下各实例的唯一标识，一般华为云租户无需携带该参数，仅在物理多租场景下从管理面访问API时需要携带该参数。

        :param instance_id: The instance_id of this ListRulesRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def app_id(self):
        """Gets the app_id of this ListRulesRequest.

        **参数说明**：资源空间ID。此参数为非必选参数，存在多资源空间的用户需要使用该接口时，可以携带该参数查询指定资源空间下的规则列表，不携带该参数则会查询该用户下所有规则列表。 **取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :return: The app_id of this ListRulesRequest.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this ListRulesRequest.

        **参数说明**：资源空间ID。此参数为非必选参数，存在多资源空间的用户需要使用该接口时，可以携带该参数查询指定资源空间下的规则列表，不携带该参数则会查询该用户下所有规则列表。 **取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :param app_id: The app_id of this ListRulesRequest.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def rule_type(self):
        """Gets the rule_type of this ListRulesRequest.

        **参数说明**：规则类型。此参数为非必选参数，指定对应的规则类型结果进行返回，不携带该参数则会返回所有类型规则。 **取值范围**： - DEVICE_LINKAGE - DATA_FORWARDING

        :return: The rule_type of this ListRulesRequest.
        :rtype: str
        """
        return self._rule_type

    @rule_type.setter
    def rule_type(self, rule_type):
        """Sets the rule_type of this ListRulesRequest.

        **参数说明**：规则类型。此参数为非必选参数，指定对应的规则类型结果进行返回，不携带该参数则会返回所有类型规则。 **取值范围**： - DEVICE_LINKAGE - DATA_FORWARDING

        :param rule_type: The rule_type of this ListRulesRequest.
        :type rule_type: str
        """
        self._rule_type = rule_type

    @property
    def limit(self):
        """Gets the limit of this ListRulesRequest.

        **参数说明**：分页查询时每页显示的记录数，查询结果根据limit进行分页。 **取值范围**：1-50的整数，默认值为10。

        :return: The limit of this ListRulesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListRulesRequest.

        **参数说明**：分页查询时每页显示的记录数，查询结果根据limit进行分页。 **取值范围**：1-50的整数，默认值为10。

        :param limit: The limit of this ListRulesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListRulesRequest.

        **参数说明**：上一次分页查询结果中最后一条记录的ID，在上一次分页查询时由物联网平台返回获得。分页查询时物联网平台是按marker也就是记录ID降序查询的，越新的数据记录ID也会越大。若填写marker，则本次只查询记录ID小于marker的数据记录。若不填写，则从记录ID最大也就是最新的一条数据开始查询。如果需要依次查询所有数据，则每次查询时必须填写上一次查询响应中的marker值。 **取值范围**：长度为24的十六进制字符串，默认值为ffffffffffffffffffffffff。

        :return: The marker of this ListRulesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListRulesRequest.

        **参数说明**：上一次分页查询结果中最后一条记录的ID，在上一次分页查询时由物联网平台返回获得。分页查询时物联网平台是按marker也就是记录ID降序查询的，越新的数据记录ID也会越大。若填写marker，则本次只查询记录ID小于marker的数据记录。若不填写，则从记录ID最大也就是最新的一条数据开始查询。如果需要依次查询所有数据，则每次查询时必须填写上一次查询响应中的marker值。 **取值范围**：长度为24的十六进制字符串，默认值为ffffffffffffffffffffffff。

        :param marker: The marker of this ListRulesRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def offset(self):
        """Gets the offset of this ListRulesRequest.

        **参数说明**：表示从marker后偏移offset条记录开始查询。默认为0，取值范围为0-500的整数。当offset为0时，表示从marker后第一条记录开始输出。限制offset最大值是出于API性能考虑，您可以搭配marker使用该参数实现翻页，例如每页50条记录，1-11页内都可以直接使用offset跳转到指定页，但到11页后，由于offset限制为500，您需要使用第11页返回的marker作为下次查询的marker，以实现翻页到12-22页。 **取值范围**：0-500的整数，默认为0。

        :return: The offset of this ListRulesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListRulesRequest.

        **参数说明**：表示从marker后偏移offset条记录开始查询。默认为0，取值范围为0-500的整数。当offset为0时，表示从marker后第一条记录开始输出。限制offset最大值是出于API性能考虑，您可以搭配marker使用该参数实现翻页，例如每页50条记录，1-11页内都可以直接使用offset跳转到指定页，但到11页后，由于offset限制为500，您需要使用第11页返回的marker作为下次查询的marker，以实现翻页到12-22页。 **取值范围**：0-500的整数，默认为0。

        :param offset: The offset of this ListRulesRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListRulesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
