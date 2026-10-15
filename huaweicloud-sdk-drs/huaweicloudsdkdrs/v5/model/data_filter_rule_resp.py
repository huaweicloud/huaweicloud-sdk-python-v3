# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataFilterRuleResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'batch_id': 'int',
        'filter_object_list': 'list[DataFilterObjectResp]',
        'filter_rules_resp': 'GeneralDataFilterResp',
        'advanced_setting_resp': 'DataFilteringAdvancedSetting'
    }

    attribute_map = {
        'batch_id': 'batch_id',
        'filter_object_list': 'filter_object_list',
        'filter_rules_resp': 'filter_rules_resp',
        'advanced_setting_resp': 'advanced_setting_resp'
    }

    def __init__(self, batch_id=None, filter_object_list=None, filter_rules_resp=None, advanced_setting_resp=None):
        r"""DataFilterRuleResp

        The model defined in huaweicloud sdk

        :param batch_id: 数据过滤规则批次ID，标识同一批次内的多个过滤对象属于同一个规则配置。
        :type batch_id: int
        :param filter_object_list: 过滤对象信息列表，列出此规则下所有需进行数据过滤的具体数据库对象
        :type filter_object_list: list[:class:`huaweicloudsdkdrs.v5.DataFilterObjectResp`]
        :param filter_rules_resp: 
        :type filter_rules_resp: :class:`huaweicloudsdkdrs.v5.GeneralDataFilterResp`
        :param advanced_setting_resp: 
        :type advanced_setting_resp: :class:`huaweicloudsdkdrs.v5.DataFilteringAdvancedSetting`
        """
        
        

        self._batch_id = None
        self._filter_object_list = None
        self._filter_rules_resp = None
        self._advanced_setting_resp = None
        self.discriminator = None

        if batch_id is not None:
            self.batch_id = batch_id
        if filter_object_list is not None:
            self.filter_object_list = filter_object_list
        if filter_rules_resp is not None:
            self.filter_rules_resp = filter_rules_resp
        if advanced_setting_resp is not None:
            self.advanced_setting_resp = advanced_setting_resp

    @property
    def batch_id(self):
        r"""Gets the batch_id of this DataFilterRuleResp.

        数据过滤规则批次ID，标识同一批次内的多个过滤对象属于同一个规则配置。

        :return: The batch_id of this DataFilterRuleResp.
        :rtype: int
        """
        return self._batch_id

    @batch_id.setter
    def batch_id(self, batch_id):
        r"""Sets the batch_id of this DataFilterRuleResp.

        数据过滤规则批次ID，标识同一批次内的多个过滤对象属于同一个规则配置。

        :param batch_id: The batch_id of this DataFilterRuleResp.
        :type batch_id: int
        """
        self._batch_id = batch_id

    @property
    def filter_object_list(self):
        r"""Gets the filter_object_list of this DataFilterRuleResp.

        过滤对象信息列表，列出此规则下所有需进行数据过滤的具体数据库对象

        :return: The filter_object_list of this DataFilterRuleResp.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.DataFilterObjectResp`]
        """
        return self._filter_object_list

    @filter_object_list.setter
    def filter_object_list(self, filter_object_list):
        r"""Sets the filter_object_list of this DataFilterRuleResp.

        过滤对象信息列表，列出此规则下所有需进行数据过滤的具体数据库对象

        :param filter_object_list: The filter_object_list of this DataFilterRuleResp.
        :type filter_object_list: list[:class:`huaweicloudsdkdrs.v5.DataFilterObjectResp`]
        """
        self._filter_object_list = filter_object_list

    @property
    def filter_rules_resp(self):
        r"""Gets the filter_rules_resp of this DataFilterRuleResp.

        :return: The filter_rules_resp of this DataFilterRuleResp.
        :rtype: :class:`huaweicloudsdkdrs.v5.GeneralDataFilterResp`
        """
        return self._filter_rules_resp

    @filter_rules_resp.setter
    def filter_rules_resp(self, filter_rules_resp):
        r"""Sets the filter_rules_resp of this DataFilterRuleResp.

        :param filter_rules_resp: The filter_rules_resp of this DataFilterRuleResp.
        :type filter_rules_resp: :class:`huaweicloudsdkdrs.v5.GeneralDataFilterResp`
        """
        self._filter_rules_resp = filter_rules_resp

    @property
    def advanced_setting_resp(self):
        r"""Gets the advanced_setting_resp of this DataFilterRuleResp.

        :return: The advanced_setting_resp of this DataFilterRuleResp.
        :rtype: :class:`huaweicloudsdkdrs.v5.DataFilteringAdvancedSetting`
        """
        return self._advanced_setting_resp

    @advanced_setting_resp.setter
    def advanced_setting_resp(self, advanced_setting_resp):
        r"""Sets the advanced_setting_resp of this DataFilterRuleResp.

        :param advanced_setting_resp: The advanced_setting_resp of this DataFilterRuleResp.
        :type advanced_setting_resp: :class:`huaweicloudsdkdrs.v5.DataFilteringAdvancedSetting`
        """
        self._advanced_setting_resp = advanced_setting_resp

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
        if not isinstance(other, DataFilterRuleResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
