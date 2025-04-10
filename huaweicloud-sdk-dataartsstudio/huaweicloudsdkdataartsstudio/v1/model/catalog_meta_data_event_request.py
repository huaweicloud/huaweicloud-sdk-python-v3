# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CatalogMetaDataEventRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'engine': 'str',
        'engine_version': 'str',
        'instance_id': 'str',
        'project_id': 'str',
        'events': 'list[CatalogMetaDataEventInfo]'
    }

    attribute_map = {
        'engine': 'engine',
        'engine_version': 'engine_version',
        'instance_id': 'instance_id',
        'project_id': 'project_id',
        'events': 'events'
    }

    def __init__(self, engine=None, engine_version=None, instance_id=None, project_id=None, events=None):
        r"""CatalogMetaDataEventRequest

        The model defined in huaweicloud sdk

        :param engine: 引擎服务名称,DLI DWS MRS
        :type engine: str
        :param engine_version: 引擎版本信息
        :type engine_version: str
        :param instance_id: 引擎的实例ID, MRS DWS必填
        :type instance_id: str
        :param project_id: 项目ID，DLI必填
        :type project_id: str
        :param events: 资产信息
        :type events: list[:class:`huaweicloudsdkdataartsstudio.v1.CatalogMetaDataEventInfo`]
        """
        
        

        self._engine = None
        self._engine_version = None
        self._instance_id = None
        self._project_id = None
        self._events = None
        self.discriminator = None

        if engine is not None:
            self.engine = engine
        if engine_version is not None:
            self.engine_version = engine_version
        if instance_id is not None:
            self.instance_id = instance_id
        if project_id is not None:
            self.project_id = project_id
        if events is not None:
            self.events = events

    @property
    def engine(self):
        r"""Gets the engine of this CatalogMetaDataEventRequest.

        引擎服务名称,DLI DWS MRS

        :return: The engine of this CatalogMetaDataEventRequest.
        :rtype: str
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        r"""Sets the engine of this CatalogMetaDataEventRequest.

        引擎服务名称,DLI DWS MRS

        :param engine: The engine of this CatalogMetaDataEventRequest.
        :type engine: str
        """
        self._engine = engine

    @property
    def engine_version(self):
        r"""Gets the engine_version of this CatalogMetaDataEventRequest.

        引擎版本信息

        :return: The engine_version of this CatalogMetaDataEventRequest.
        :rtype: str
        """
        return self._engine_version

    @engine_version.setter
    def engine_version(self, engine_version):
        r"""Sets the engine_version of this CatalogMetaDataEventRequest.

        引擎版本信息

        :param engine_version: The engine_version of this CatalogMetaDataEventRequest.
        :type engine_version: str
        """
        self._engine_version = engine_version

    @property
    def instance_id(self):
        r"""Gets the instance_id of this CatalogMetaDataEventRequest.

        引擎的实例ID, MRS DWS必填

        :return: The instance_id of this CatalogMetaDataEventRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this CatalogMetaDataEventRequest.

        引擎的实例ID, MRS DWS必填

        :param instance_id: The instance_id of this CatalogMetaDataEventRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def project_id(self):
        r"""Gets the project_id of this CatalogMetaDataEventRequest.

        项目ID，DLI必填

        :return: The project_id of this CatalogMetaDataEventRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this CatalogMetaDataEventRequest.

        项目ID，DLI必填

        :param project_id: The project_id of this CatalogMetaDataEventRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def events(self):
        r"""Gets the events of this CatalogMetaDataEventRequest.

        资产信息

        :return: The events of this CatalogMetaDataEventRequest.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.CatalogMetaDataEventInfo`]
        """
        return self._events

    @events.setter
    def events(self, events):
        r"""Sets the events of this CatalogMetaDataEventRequest.

        资产信息

        :param events: The events of this CatalogMetaDataEventRequest.
        :type events: list[:class:`huaweicloudsdkdataartsstudio.v1.CatalogMetaDataEventInfo`]
        """
        self._events = events

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
        if not isinstance(other, CatalogMetaDataEventRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
