# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDataStoreFlavorDetailRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'datastore_id': 'str',
        'datastore_version_id': 'str'
    }

    attribute_map = {
        'datastore_id': 'datastore_id',
        'datastore_version_id': 'datastore_version_id'
    }

    def __init__(self, datastore_id=None, datastore_version_id=None):
        r"""ShowDataStoreFlavorDetailRequest

        The model defined in huaweicloud sdk

        :param datastore_id: **参数解释**： 引擎类型id。 **约束限制**： 不涉及 **取值范围**： Elasticsearch：cf7e2c8f-096c-4fcf-b174-1ebe060679fb。 Opensearch：07ec9f86-ec2f-49e7-8913-373003aedf32。 Logstash: 575276bb-87e5-4e18-8e1e-e748d8ad3a06。 **默认取值**： 不涉及
        :type datastore_id: str
        :param datastore_version_id: **参数解释**： 引擎类型id。 **约束限制**： 不涉及 **取值范围**： Elasticsearch 7.10.2：01f53413-0a58-4b0c-848a-f625846bae23。 Opensearch 2.19.0：11a9df5c-711f-496c-866d-a4521c179671。 Logstash 7.10.0: f5609cf0-3514-49ef-87db-a3df2858a46f。 **默认取值**： 不涉及
        :type datastore_version_id: str
        """
        
        

        self._datastore_id = None
        self._datastore_version_id = None
        self.discriminator = None

        self.datastore_id = datastore_id
        if datastore_version_id is not None:
            self.datastore_version_id = datastore_version_id

    @property
    def datastore_id(self):
        r"""Gets the datastore_id of this ShowDataStoreFlavorDetailRequest.

        **参数解释**： 引擎类型id。 **约束限制**： 不涉及 **取值范围**： Elasticsearch：cf7e2c8f-096c-4fcf-b174-1ebe060679fb。 Opensearch：07ec9f86-ec2f-49e7-8913-373003aedf32。 Logstash: 575276bb-87e5-4e18-8e1e-e748d8ad3a06。 **默认取值**： 不涉及

        :return: The datastore_id of this ShowDataStoreFlavorDetailRequest.
        :rtype: str
        """
        return self._datastore_id

    @datastore_id.setter
    def datastore_id(self, datastore_id):
        r"""Sets the datastore_id of this ShowDataStoreFlavorDetailRequest.

        **参数解释**： 引擎类型id。 **约束限制**： 不涉及 **取值范围**： Elasticsearch：cf7e2c8f-096c-4fcf-b174-1ebe060679fb。 Opensearch：07ec9f86-ec2f-49e7-8913-373003aedf32。 Logstash: 575276bb-87e5-4e18-8e1e-e748d8ad3a06。 **默认取值**： 不涉及

        :param datastore_id: The datastore_id of this ShowDataStoreFlavorDetailRequest.
        :type datastore_id: str
        """
        self._datastore_id = datastore_id

    @property
    def datastore_version_id(self):
        r"""Gets the datastore_version_id of this ShowDataStoreFlavorDetailRequest.

        **参数解释**： 引擎类型id。 **约束限制**： 不涉及 **取值范围**： Elasticsearch 7.10.2：01f53413-0a58-4b0c-848a-f625846bae23。 Opensearch 2.19.0：11a9df5c-711f-496c-866d-a4521c179671。 Logstash 7.10.0: f5609cf0-3514-49ef-87db-a3df2858a46f。 **默认取值**： 不涉及

        :return: The datastore_version_id of this ShowDataStoreFlavorDetailRequest.
        :rtype: str
        """
        return self._datastore_version_id

    @datastore_version_id.setter
    def datastore_version_id(self, datastore_version_id):
        r"""Sets the datastore_version_id of this ShowDataStoreFlavorDetailRequest.

        **参数解释**： 引擎类型id。 **约束限制**： 不涉及 **取值范围**： Elasticsearch 7.10.2：01f53413-0a58-4b0c-848a-f625846bae23。 Opensearch 2.19.0：11a9df5c-711f-496c-866d-a4521c179671。 Logstash 7.10.0: f5609cf0-3514-49ef-87db-a3df2858a46f。 **默认取值**： 不涉及

        :param datastore_version_id: The datastore_version_id of this ShowDataStoreFlavorDetailRequest.
        :type datastore_version_id: str
        """
        self._datastore_version_id = datastore_version_id

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
        if not isinstance(other, ShowDataStoreFlavorDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
