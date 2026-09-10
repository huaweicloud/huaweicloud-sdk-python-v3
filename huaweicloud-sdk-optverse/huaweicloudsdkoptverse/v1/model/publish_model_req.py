# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PublishModelReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'train_job_id': 'str',
        'name': 'str',
        'description': 'str',
        'asset_location': 'str',
        'chat_id': 'str',
        'asset_version': 'str',
        'external_version': 'str',
        'asset_type': 'str',
        'sub_asset_type': 'str'
    }

    attribute_map = {
        'train_job_id': 'train_job_id',
        'name': 'name',
        'description': 'description',
        'asset_location': 'asset_location',
        'chat_id': 'chat_id',
        'asset_version': 'asset_version',
        'external_version': 'external_version',
        'asset_type': 'asset_type',
        'sub_asset_type': 'sub_asset_type'
    }

    def __init__(self, train_job_id=None, name=None, description=None, asset_location=None, chat_id=None, asset_version=None, external_version=None, asset_type=None, sub_asset_type=None):
        r"""PublishModelReq

        The model defined in huaweicloud sdk

        :param train_job_id: **参数解释**： 训练任务ID。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type train_job_id: str
        :param name: **参数解释**： 模型名称。 **约束限制**： 不涉及 **取值范围**： 长度为[1-128]个字符。 **默认取值**： 不涉及 
        :type name: str
        :param description: **参数解释**： 模型名称。 **约束限制**： 不涉及 **取值范围**： 长度为[1-2048]个字符。 **默认取值**： 不涉及 
        :type description: str
        :param asset_location: **参数解释**： 模型在OBS存储位置。 **约束限制**： 不涉及 **取值范围**： 长度为[1-512]个字符。 **默认取值**： 不涉及 
        :type asset_location: str
        :param chat_id: **参数解释**： 对话id。 **约束限制**： 不涉及 **取值范围**： 长度为[1-64]个字符。 **默认取值**： 不涉及 
        :type chat_id: str
        :param asset_version: **参数解释**： 模型版本。 **约束限制**： 不涉及 **取值范围**： 长度为[1-64]个字符。 **默认取值**： 不涉及 
        :type asset_version: str
        :param external_version: **参数解释**： 模型对外显示版本。 **约束限制**： 不涉及 **取值范围**： 长度为[1-64]个字符。 **默认取值**： 不涉及 
        :type external_version: str
        :param asset_type: **参数解释**： 模型类型。 **约束限制**： 不涉及 **取值范围**： 长度为[1-64]个字符。 **默认取值**： 不涉及 
        :type asset_type: str
        :param sub_asset_type: **参数解释**： 模型子类型。 **约束限制**： 不涉及 **取值范围**： 长度为[1-64]个字符。 **默认取值**： 不涉及 
        :type sub_asset_type: str
        """
        
        

        self._train_job_id = None
        self._name = None
        self._description = None
        self._asset_location = None
        self._chat_id = None
        self._asset_version = None
        self._external_version = None
        self._asset_type = None
        self._sub_asset_type = None
        self.discriminator = None

        if train_job_id is not None:
            self.train_job_id = train_job_id
        self.name = name
        if description is not None:
            self.description = description
        if asset_location is not None:
            self.asset_location = asset_location
        if chat_id is not None:
            self.chat_id = chat_id
        if asset_version is not None:
            self.asset_version = asset_version
        if external_version is not None:
            self.external_version = external_version
        if asset_type is not None:
            self.asset_type = asset_type
        if sub_asset_type is not None:
            self.sub_asset_type = sub_asset_type

    @property
    def train_job_id(self):
        r"""Gets the train_job_id of this PublishModelReq.

        **参数解释**： 训练任务ID。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The train_job_id of this PublishModelReq.
        :rtype: str
        """
        return self._train_job_id

    @train_job_id.setter
    def train_job_id(self, train_job_id):
        r"""Sets the train_job_id of this PublishModelReq.

        **参数解释**： 训练任务ID。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param train_job_id: The train_job_id of this PublishModelReq.
        :type train_job_id: str
        """
        self._train_job_id = train_job_id

    @property
    def name(self):
        r"""Gets the name of this PublishModelReq.

        **参数解释**： 模型名称。 **约束限制**： 不涉及 **取值范围**： 长度为[1-128]个字符。 **默认取值**： 不涉及 

        :return: The name of this PublishModelReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this PublishModelReq.

        **参数解释**： 模型名称。 **约束限制**： 不涉及 **取值范围**： 长度为[1-128]个字符。 **默认取值**： 不涉及 

        :param name: The name of this PublishModelReq.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this PublishModelReq.

        **参数解释**： 模型名称。 **约束限制**： 不涉及 **取值范围**： 长度为[1-2048]个字符。 **默认取值**： 不涉及 

        :return: The description of this PublishModelReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this PublishModelReq.

        **参数解释**： 模型名称。 **约束限制**： 不涉及 **取值范围**： 长度为[1-2048]个字符。 **默认取值**： 不涉及 

        :param description: The description of this PublishModelReq.
        :type description: str
        """
        self._description = description

    @property
    def asset_location(self):
        r"""Gets the asset_location of this PublishModelReq.

        **参数解释**： 模型在OBS存储位置。 **约束限制**： 不涉及 **取值范围**： 长度为[1-512]个字符。 **默认取值**： 不涉及 

        :return: The asset_location of this PublishModelReq.
        :rtype: str
        """
        return self._asset_location

    @asset_location.setter
    def asset_location(self, asset_location):
        r"""Sets the asset_location of this PublishModelReq.

        **参数解释**： 模型在OBS存储位置。 **约束限制**： 不涉及 **取值范围**： 长度为[1-512]个字符。 **默认取值**： 不涉及 

        :param asset_location: The asset_location of this PublishModelReq.
        :type asset_location: str
        """
        self._asset_location = asset_location

    @property
    def chat_id(self):
        r"""Gets the chat_id of this PublishModelReq.

        **参数解释**： 对话id。 **约束限制**： 不涉及 **取值范围**： 长度为[1-64]个字符。 **默认取值**： 不涉及 

        :return: The chat_id of this PublishModelReq.
        :rtype: str
        """
        return self._chat_id

    @chat_id.setter
    def chat_id(self, chat_id):
        r"""Sets the chat_id of this PublishModelReq.

        **参数解释**： 对话id。 **约束限制**： 不涉及 **取值范围**： 长度为[1-64]个字符。 **默认取值**： 不涉及 

        :param chat_id: The chat_id of this PublishModelReq.
        :type chat_id: str
        """
        self._chat_id = chat_id

    @property
    def asset_version(self):
        r"""Gets the asset_version of this PublishModelReq.

        **参数解释**： 模型版本。 **约束限制**： 不涉及 **取值范围**： 长度为[1-64]个字符。 **默认取值**： 不涉及 

        :return: The asset_version of this PublishModelReq.
        :rtype: str
        """
        return self._asset_version

    @asset_version.setter
    def asset_version(self, asset_version):
        r"""Sets the asset_version of this PublishModelReq.

        **参数解释**： 模型版本。 **约束限制**： 不涉及 **取值范围**： 长度为[1-64]个字符。 **默认取值**： 不涉及 

        :param asset_version: The asset_version of this PublishModelReq.
        :type asset_version: str
        """
        self._asset_version = asset_version

    @property
    def external_version(self):
        r"""Gets the external_version of this PublishModelReq.

        **参数解释**： 模型对外显示版本。 **约束限制**： 不涉及 **取值范围**： 长度为[1-64]个字符。 **默认取值**： 不涉及 

        :return: The external_version of this PublishModelReq.
        :rtype: str
        """
        return self._external_version

    @external_version.setter
    def external_version(self, external_version):
        r"""Sets the external_version of this PublishModelReq.

        **参数解释**： 模型对外显示版本。 **约束限制**： 不涉及 **取值范围**： 长度为[1-64]个字符。 **默认取值**： 不涉及 

        :param external_version: The external_version of this PublishModelReq.
        :type external_version: str
        """
        self._external_version = external_version

    @property
    def asset_type(self):
        r"""Gets the asset_type of this PublishModelReq.

        **参数解释**： 模型类型。 **约束限制**： 不涉及 **取值范围**： 长度为[1-64]个字符。 **默认取值**： 不涉及 

        :return: The asset_type of this PublishModelReq.
        :rtype: str
        """
        return self._asset_type

    @asset_type.setter
    def asset_type(self, asset_type):
        r"""Sets the asset_type of this PublishModelReq.

        **参数解释**： 模型类型。 **约束限制**： 不涉及 **取值范围**： 长度为[1-64]个字符。 **默认取值**： 不涉及 

        :param asset_type: The asset_type of this PublishModelReq.
        :type asset_type: str
        """
        self._asset_type = asset_type

    @property
    def sub_asset_type(self):
        r"""Gets the sub_asset_type of this PublishModelReq.

        **参数解释**： 模型子类型。 **约束限制**： 不涉及 **取值范围**： 长度为[1-64]个字符。 **默认取值**： 不涉及 

        :return: The sub_asset_type of this PublishModelReq.
        :rtype: str
        """
        return self._sub_asset_type

    @sub_asset_type.setter
    def sub_asset_type(self, sub_asset_type):
        r"""Sets the sub_asset_type of this PublishModelReq.

        **参数解释**： 模型子类型。 **约束限制**： 不涉及 **取值范围**： 长度为[1-64]个字符。 **默认取值**： 不涉及 

        :param sub_asset_type: The sub_asset_type of this PublishModelReq.
        :type sub_asset_type: str
        """
        self._sub_asset_type = sub_asset_type

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
        if not isinstance(other, PublishModelReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
