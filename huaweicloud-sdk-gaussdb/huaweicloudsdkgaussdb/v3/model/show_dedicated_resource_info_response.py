# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDedicatedResourceInfoResponse(SdkResponse):

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
        'engine_name': 'str',
        'availability_zone_ids': 'list[str]',
        'architecture': 'str',
        'status': 'str',
        'dedicated_compute_info': 'DedicatedComputeInfo',
        'dedicated_storage_info': 'DedicatedStorageInfo'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'engine_name': 'engine_name',
        'availability_zone_ids': 'availability_zone_ids',
        'architecture': 'architecture',
        'status': 'status',
        'dedicated_compute_info': 'dedicated_compute_info',
        'dedicated_storage_info': 'dedicated_storage_info'
    }

    def __init__(self, id=None, name=None, engine_name=None, availability_zone_ids=None, architecture=None, status=None, dedicated_compute_info=None, dedicated_storage_info=None):
        """ShowDedicatedResourceInfoResponse

        The model defined in huaweicloud sdk

        :param id: 专属资源池ID。
        :type id: str
        :param name: 专属资源池名称。
        :type name: str
        :param engine_name: 引擎名称。
        :type engine_name: str
        :param availability_zone_ids: 可用区。
        :type availability_zone_ids: list[str]
        :param architecture: 资源规格类型。
        :type architecture: str
        :param status: 专属资源池状态。
        :type status: str
        :param dedicated_compute_info: 
        :type dedicated_compute_info: :class:`huaweicloudsdkgaussdb.v3.DedicatedComputeInfo`
        :param dedicated_storage_info: 
        :type dedicated_storage_info: :class:`huaweicloudsdkgaussdb.v3.DedicatedStorageInfo`
        """
        
        super(ShowDedicatedResourceInfoResponse, self).__init__()

        self._id = None
        self._name = None
        self._engine_name = None
        self._availability_zone_ids = None
        self._architecture = None
        self._status = None
        self._dedicated_compute_info = None
        self._dedicated_storage_info = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if engine_name is not None:
            self.engine_name = engine_name
        if availability_zone_ids is not None:
            self.availability_zone_ids = availability_zone_ids
        if architecture is not None:
            self.architecture = architecture
        if status is not None:
            self.status = status
        if dedicated_compute_info is not None:
            self.dedicated_compute_info = dedicated_compute_info
        if dedicated_storage_info is not None:
            self.dedicated_storage_info = dedicated_storage_info

    @property
    def id(self):
        """Gets the id of this ShowDedicatedResourceInfoResponse.

        专属资源池ID。

        :return: The id of this ShowDedicatedResourceInfoResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowDedicatedResourceInfoResponse.

        专属资源池ID。

        :param id: The id of this ShowDedicatedResourceInfoResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ShowDedicatedResourceInfoResponse.

        专属资源池名称。

        :return: The name of this ShowDedicatedResourceInfoResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowDedicatedResourceInfoResponse.

        专属资源池名称。

        :param name: The name of this ShowDedicatedResourceInfoResponse.
        :type name: str
        """
        self._name = name

    @property
    def engine_name(self):
        """Gets the engine_name of this ShowDedicatedResourceInfoResponse.

        引擎名称。

        :return: The engine_name of this ShowDedicatedResourceInfoResponse.
        :rtype: str
        """
        return self._engine_name

    @engine_name.setter
    def engine_name(self, engine_name):
        """Sets the engine_name of this ShowDedicatedResourceInfoResponse.

        引擎名称。

        :param engine_name: The engine_name of this ShowDedicatedResourceInfoResponse.
        :type engine_name: str
        """
        self._engine_name = engine_name

    @property
    def availability_zone_ids(self):
        """Gets the availability_zone_ids of this ShowDedicatedResourceInfoResponse.

        可用区。

        :return: The availability_zone_ids of this ShowDedicatedResourceInfoResponse.
        :rtype: list[str]
        """
        return self._availability_zone_ids

    @availability_zone_ids.setter
    def availability_zone_ids(self, availability_zone_ids):
        """Sets the availability_zone_ids of this ShowDedicatedResourceInfoResponse.

        可用区。

        :param availability_zone_ids: The availability_zone_ids of this ShowDedicatedResourceInfoResponse.
        :type availability_zone_ids: list[str]
        """
        self._availability_zone_ids = availability_zone_ids

    @property
    def architecture(self):
        """Gets the architecture of this ShowDedicatedResourceInfoResponse.

        资源规格类型。

        :return: The architecture of this ShowDedicatedResourceInfoResponse.
        :rtype: str
        """
        return self._architecture

    @architecture.setter
    def architecture(self, architecture):
        """Sets the architecture of this ShowDedicatedResourceInfoResponse.

        资源规格类型。

        :param architecture: The architecture of this ShowDedicatedResourceInfoResponse.
        :type architecture: str
        """
        self._architecture = architecture

    @property
    def status(self):
        """Gets the status of this ShowDedicatedResourceInfoResponse.

        专属资源池状态。

        :return: The status of this ShowDedicatedResourceInfoResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowDedicatedResourceInfoResponse.

        专属资源池状态。

        :param status: The status of this ShowDedicatedResourceInfoResponse.
        :type status: str
        """
        self._status = status

    @property
    def dedicated_compute_info(self):
        """Gets the dedicated_compute_info of this ShowDedicatedResourceInfoResponse.

        :return: The dedicated_compute_info of this ShowDedicatedResourceInfoResponse.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.DedicatedComputeInfo`
        """
        return self._dedicated_compute_info

    @dedicated_compute_info.setter
    def dedicated_compute_info(self, dedicated_compute_info):
        """Sets the dedicated_compute_info of this ShowDedicatedResourceInfoResponse.

        :param dedicated_compute_info: The dedicated_compute_info of this ShowDedicatedResourceInfoResponse.
        :type dedicated_compute_info: :class:`huaweicloudsdkgaussdb.v3.DedicatedComputeInfo`
        """
        self._dedicated_compute_info = dedicated_compute_info

    @property
    def dedicated_storage_info(self):
        """Gets the dedicated_storage_info of this ShowDedicatedResourceInfoResponse.

        :return: The dedicated_storage_info of this ShowDedicatedResourceInfoResponse.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.DedicatedStorageInfo`
        """
        return self._dedicated_storage_info

    @dedicated_storage_info.setter
    def dedicated_storage_info(self, dedicated_storage_info):
        """Sets the dedicated_storage_info of this ShowDedicatedResourceInfoResponse.

        :param dedicated_storage_info: The dedicated_storage_info of this ShowDedicatedResourceInfoResponse.
        :type dedicated_storage_info: :class:`huaweicloudsdkgaussdb.v3.DedicatedStorageInfo`
        """
        self._dedicated_storage_info = dedicated_storage_info

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
        if not isinstance(other, ShowDedicatedResourceInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
