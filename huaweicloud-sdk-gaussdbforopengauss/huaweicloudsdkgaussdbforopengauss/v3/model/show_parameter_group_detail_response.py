# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowParameterGroupDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'description': 'str',
        'engine_version': 'str',
        'instance_mode': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'configuration_parameters': 'list[ParaGroupParameterResult]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'engine_version': 'engine_version',
        'instance_mode': 'instance_mode',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'configuration_parameters': 'configuration_parameters'
    }

    def __init__(self, id=None, name=None, description=None, engine_version=None, instance_mode=None, created_at=None, updated_at=None, configuration_parameters=None):
        r"""ShowParameterGroupDetailResponse

        The model defined in huaweicloud sdk

        :param id: 参数模板ID。
        :type id: str
        :param name: 参数模板名称。
        :type name: str
        :param description: 参数模板描述。
        :type description: str
        :param engine_version: 引擎版本。 [数据库版本。支持V2.0-2.3版本，取值为“V2.0-2.3”]。
        :type engine_version: str
        :param instance_mode: 实例部署形态。independent：独立；ha：主备。
        :type instance_mode: str
        :param created_at: 创建时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。
        :type created_at: str
        :param updated_at: 修改时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。
        :type updated_at: str
        :param configuration_parameters: 参数详情。
        :type configuration_parameters: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.ParaGroupParameterResult`]
        """
        
        super(ShowParameterGroupDetailResponse, self).__init__()

        self._id = None
        self._name = None
        self._description = None
        self._engine_version = None
        self._instance_mode = None
        self._created_at = None
        self._updated_at = None
        self._configuration_parameters = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if engine_version is not None:
            self.engine_version = engine_version
        if instance_mode is not None:
            self.instance_mode = instance_mode
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if configuration_parameters is not None:
            self.configuration_parameters = configuration_parameters

    @property
    def id(self):
        r"""Gets the id of this ShowParameterGroupDetailResponse.

        参数模板ID。

        :return: The id of this ShowParameterGroupDetailResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowParameterGroupDetailResponse.

        参数模板ID。

        :param id: The id of this ShowParameterGroupDetailResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ShowParameterGroupDetailResponse.

        参数模板名称。

        :return: The name of this ShowParameterGroupDetailResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowParameterGroupDetailResponse.

        参数模板名称。

        :param name: The name of this ShowParameterGroupDetailResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ShowParameterGroupDetailResponse.

        参数模板描述。

        :return: The description of this ShowParameterGroupDetailResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowParameterGroupDetailResponse.

        参数模板描述。

        :param description: The description of this ShowParameterGroupDetailResponse.
        :type description: str
        """
        self._description = description

    @property
    def engine_version(self):
        r"""Gets the engine_version of this ShowParameterGroupDetailResponse.

        引擎版本。 [数据库版本。支持V2.0-2.3版本，取值为“V2.0-2.3”]。

        :return: The engine_version of this ShowParameterGroupDetailResponse.
        :rtype: str
        """
        return self._engine_version

    @engine_version.setter
    def engine_version(self, engine_version):
        r"""Sets the engine_version of this ShowParameterGroupDetailResponse.

        引擎版本。 [数据库版本。支持V2.0-2.3版本，取值为“V2.0-2.3”]。

        :param engine_version: The engine_version of this ShowParameterGroupDetailResponse.
        :type engine_version: str
        """
        self._engine_version = engine_version

    @property
    def instance_mode(self):
        r"""Gets the instance_mode of this ShowParameterGroupDetailResponse.

        实例部署形态。independent：独立；ha：主备。

        :return: The instance_mode of this ShowParameterGroupDetailResponse.
        :rtype: str
        """
        return self._instance_mode

    @instance_mode.setter
    def instance_mode(self, instance_mode):
        r"""Sets the instance_mode of this ShowParameterGroupDetailResponse.

        实例部署形态。independent：独立；ha：主备。

        :param instance_mode: The instance_mode of this ShowParameterGroupDetailResponse.
        :type instance_mode: str
        """
        self._instance_mode = instance_mode

    @property
    def created_at(self):
        r"""Gets the created_at of this ShowParameterGroupDetailResponse.

        创建时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :return: The created_at of this ShowParameterGroupDetailResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ShowParameterGroupDetailResponse.

        创建时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :param created_at: The created_at of this ShowParameterGroupDetailResponse.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this ShowParameterGroupDetailResponse.

        修改时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :return: The updated_at of this ShowParameterGroupDetailResponse.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this ShowParameterGroupDetailResponse.

        修改时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :param updated_at: The updated_at of this ShowParameterGroupDetailResponse.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def configuration_parameters(self):
        r"""Gets the configuration_parameters of this ShowParameterGroupDetailResponse.

        参数详情。

        :return: The configuration_parameters of this ShowParameterGroupDetailResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.ParaGroupParameterResult`]
        """
        return self._configuration_parameters

    @configuration_parameters.setter
    def configuration_parameters(self, configuration_parameters):
        r"""Sets the configuration_parameters of this ShowParameterGroupDetailResponse.

        参数详情。

        :param configuration_parameters: The configuration_parameters of this ShowParameterGroupDetailResponse.
        :type configuration_parameters: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.ParaGroupParameterResult`]
        """
        self._configuration_parameters = configuration_parameters

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
        if not isinstance(other, ShowParameterGroupDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
