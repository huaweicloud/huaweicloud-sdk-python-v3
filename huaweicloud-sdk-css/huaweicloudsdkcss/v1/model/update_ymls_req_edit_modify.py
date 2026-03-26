# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateYmlsReqEditModify:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'elasticsearch_yml': 'object',
        'kibana_yml': 'object'
    }

    attribute_map = {
        'elasticsearch_yml': 'elasticsearch.yml',
        'kibana_yml': 'kibana.yml'
    }

    def __init__(self, elasticsearch_yml=None, kibana_yml=None):
        r"""UpdateYmlsReqEditModify

        The model defined in huaweicloud sdk

        :param elasticsearch_yml: **参数解释**： 参数配置列表，值为需要修改的json数据，OpenSearch集群也使用此参数，即修改opensearch.yml时，这里也是填写elasticsearch.yml。 **约束限制**： 不涉及
        :type elasticsearch_yml: object
        :param kibana_yml: **参数解释**： 参数配置列表，值为需要修改的json数据。OpenSearch集群也使用此参数，即修改opensearch_dashboards.yml时，这里也是填写kibana.yml。 **约束限制**： 不涉及
        :type kibana_yml: object
        """
        
        

        self._elasticsearch_yml = None
        self._kibana_yml = None
        self.discriminator = None

        if elasticsearch_yml is not None:
            self.elasticsearch_yml = elasticsearch_yml
        if kibana_yml is not None:
            self.kibana_yml = kibana_yml

    @property
    def elasticsearch_yml(self):
        r"""Gets the elasticsearch_yml of this UpdateYmlsReqEditModify.

        **参数解释**： 参数配置列表，值为需要修改的json数据，OpenSearch集群也使用此参数，即修改opensearch.yml时，这里也是填写elasticsearch.yml。 **约束限制**： 不涉及

        :return: The elasticsearch_yml of this UpdateYmlsReqEditModify.
        :rtype: object
        """
        return self._elasticsearch_yml

    @elasticsearch_yml.setter
    def elasticsearch_yml(self, elasticsearch_yml):
        r"""Sets the elasticsearch_yml of this UpdateYmlsReqEditModify.

        **参数解释**： 参数配置列表，值为需要修改的json数据，OpenSearch集群也使用此参数，即修改opensearch.yml时，这里也是填写elasticsearch.yml。 **约束限制**： 不涉及

        :param elasticsearch_yml: The elasticsearch_yml of this UpdateYmlsReqEditModify.
        :type elasticsearch_yml: object
        """
        self._elasticsearch_yml = elasticsearch_yml

    @property
    def kibana_yml(self):
        r"""Gets the kibana_yml of this UpdateYmlsReqEditModify.

        **参数解释**： 参数配置列表，值为需要修改的json数据。OpenSearch集群也使用此参数，即修改opensearch_dashboards.yml时，这里也是填写kibana.yml。 **约束限制**： 不涉及

        :return: The kibana_yml of this UpdateYmlsReqEditModify.
        :rtype: object
        """
        return self._kibana_yml

    @kibana_yml.setter
    def kibana_yml(self, kibana_yml):
        r"""Sets the kibana_yml of this UpdateYmlsReqEditModify.

        **参数解释**： 参数配置列表，值为需要修改的json数据。OpenSearch集群也使用此参数，即修改opensearch_dashboards.yml时，这里也是填写kibana.yml。 **约束限制**： 不涉及

        :param kibana_yml: The kibana_yml of this UpdateYmlsReqEditModify.
        :type kibana_yml: object
        """
        self._kibana_yml = kibana_yml

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
        if not isinstance(other, UpdateYmlsReqEditModify):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
