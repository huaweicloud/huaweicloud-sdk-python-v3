# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MicroServiceInfo:

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
        'instance_id': 'str',
        'service_type': 'str',
        'cse_info': 'MicroServiceInfoCSE',
        'cce_info': 'MicroServiceInfoCCE',
        'cce_service_info': 'MicroServiceInfoCCEService',
        'nacos_info': 'MicroServiceInfoNacosBase',
        'update_time': 'datetime',
        'create_time': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'instance_id': 'instance_id',
        'service_type': 'service_type',
        'cse_info': 'cse_info',
        'cce_info': 'cce_info',
        'cce_service_info': 'cce_service_info',
        'nacos_info': 'nacos_info',
        'update_time': 'update_time',
        'create_time': 'create_time'
    }

    def __init__(self, id=None, instance_id=None, service_type=None, cse_info=None, cce_info=None, cce_service_info=None, nacos_info=None, update_time=None, create_time=None):
        r"""MicroServiceInfo

        The model defined in huaweicloud sdk

        :param id: 微服务编号
        :type id: str
        :param instance_id: 实例编号
        :type instance_id: str
        :param service_type: 微服务类型： - CSE：CSE微服务注册中心 - CCE：CCE云容器引擎（工作负载） - CCE_SERVICE: CCE云容器引擎（Service） - NACOS: nacos引擎，nacos_info必填
        :type service_type: str
        :param cse_info: 
        :type cse_info: :class:`huaweicloudsdkapig.v2.MicroServiceInfoCSE`
        :param cce_info: 
        :type cce_info: :class:`huaweicloudsdkapig.v2.MicroServiceInfoCCE`
        :param cce_service_info: 
        :type cce_service_info: :class:`huaweicloudsdkapig.v2.MicroServiceInfoCCEService`
        :param nacos_info: 
        :type nacos_info: :class:`huaweicloudsdkapig.v2.MicroServiceInfoNacosBase`
        :param update_time: 微服务更新时间
        :type update_time: datetime
        :param create_time: 微服务创建时间
        :type create_time: datetime
        """
        
        

        self._id = None
        self._instance_id = None
        self._service_type = None
        self._cse_info = None
        self._cce_info = None
        self._cce_service_info = None
        self._nacos_info = None
        self._update_time = None
        self._create_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if instance_id is not None:
            self.instance_id = instance_id
        if service_type is not None:
            self.service_type = service_type
        if cse_info is not None:
            self.cse_info = cse_info
        if cce_info is not None:
            self.cce_info = cce_info
        if cce_service_info is not None:
            self.cce_service_info = cce_service_info
        if nacos_info is not None:
            self.nacos_info = nacos_info
        if update_time is not None:
            self.update_time = update_time
        if create_time is not None:
            self.create_time = create_time

    @property
    def id(self):
        r"""Gets the id of this MicroServiceInfo.

        微服务编号

        :return: The id of this MicroServiceInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this MicroServiceInfo.

        微服务编号

        :param id: The id of this MicroServiceInfo.
        :type id: str
        """
        self._id = id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this MicroServiceInfo.

        实例编号

        :return: The instance_id of this MicroServiceInfo.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this MicroServiceInfo.

        实例编号

        :param instance_id: The instance_id of this MicroServiceInfo.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def service_type(self):
        r"""Gets the service_type of this MicroServiceInfo.

        微服务类型： - CSE：CSE微服务注册中心 - CCE：CCE云容器引擎（工作负载） - CCE_SERVICE: CCE云容器引擎（Service） - NACOS: nacos引擎，nacos_info必填

        :return: The service_type of this MicroServiceInfo.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        r"""Sets the service_type of this MicroServiceInfo.

        微服务类型： - CSE：CSE微服务注册中心 - CCE：CCE云容器引擎（工作负载） - CCE_SERVICE: CCE云容器引擎（Service） - NACOS: nacos引擎，nacos_info必填

        :param service_type: The service_type of this MicroServiceInfo.
        :type service_type: str
        """
        self._service_type = service_type

    @property
    def cse_info(self):
        r"""Gets the cse_info of this MicroServiceInfo.

        :return: The cse_info of this MicroServiceInfo.
        :rtype: :class:`huaweicloudsdkapig.v2.MicroServiceInfoCSE`
        """
        return self._cse_info

    @cse_info.setter
    def cse_info(self, cse_info):
        r"""Sets the cse_info of this MicroServiceInfo.

        :param cse_info: The cse_info of this MicroServiceInfo.
        :type cse_info: :class:`huaweicloudsdkapig.v2.MicroServiceInfoCSE`
        """
        self._cse_info = cse_info

    @property
    def cce_info(self):
        r"""Gets the cce_info of this MicroServiceInfo.

        :return: The cce_info of this MicroServiceInfo.
        :rtype: :class:`huaweicloudsdkapig.v2.MicroServiceInfoCCE`
        """
        return self._cce_info

    @cce_info.setter
    def cce_info(self, cce_info):
        r"""Sets the cce_info of this MicroServiceInfo.

        :param cce_info: The cce_info of this MicroServiceInfo.
        :type cce_info: :class:`huaweicloudsdkapig.v2.MicroServiceInfoCCE`
        """
        self._cce_info = cce_info

    @property
    def cce_service_info(self):
        r"""Gets the cce_service_info of this MicroServiceInfo.

        :return: The cce_service_info of this MicroServiceInfo.
        :rtype: :class:`huaweicloudsdkapig.v2.MicroServiceInfoCCEService`
        """
        return self._cce_service_info

    @cce_service_info.setter
    def cce_service_info(self, cce_service_info):
        r"""Sets the cce_service_info of this MicroServiceInfo.

        :param cce_service_info: The cce_service_info of this MicroServiceInfo.
        :type cce_service_info: :class:`huaweicloudsdkapig.v2.MicroServiceInfoCCEService`
        """
        self._cce_service_info = cce_service_info

    @property
    def nacos_info(self):
        r"""Gets the nacos_info of this MicroServiceInfo.

        :return: The nacos_info of this MicroServiceInfo.
        :rtype: :class:`huaweicloudsdkapig.v2.MicroServiceInfoNacosBase`
        """
        return self._nacos_info

    @nacos_info.setter
    def nacos_info(self, nacos_info):
        r"""Sets the nacos_info of this MicroServiceInfo.

        :param nacos_info: The nacos_info of this MicroServiceInfo.
        :type nacos_info: :class:`huaweicloudsdkapig.v2.MicroServiceInfoNacosBase`
        """
        self._nacos_info = nacos_info

    @property
    def update_time(self):
        r"""Gets the update_time of this MicroServiceInfo.

        微服务更新时间

        :return: The update_time of this MicroServiceInfo.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this MicroServiceInfo.

        微服务更新时间

        :param update_time: The update_time of this MicroServiceInfo.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def create_time(self):
        r"""Gets the create_time of this MicroServiceInfo.

        微服务创建时间

        :return: The create_time of this MicroServiceInfo.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this MicroServiceInfo.

        微服务创建时间

        :param create_time: The create_time of this MicroServiceInfo.
        :type create_time: datetime
        """
        self._create_time = create_time

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
        if not isinstance(other, MicroServiceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
