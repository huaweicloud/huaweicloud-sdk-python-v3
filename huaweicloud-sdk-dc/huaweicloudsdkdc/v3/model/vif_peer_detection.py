# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VifPeerDetection:

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
        'vif_peer_id': 'str',
        'project_id': 'str',
        'domain_id': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'status': 'str',
        'loss_ratio': 'int'
    }

    attribute_map = {
        'id': 'id',
        'vif_peer_id': 'vif_peer_id',
        'project_id': 'project_id',
        'domain_id': 'domain_id',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'status': 'status',
        'loss_ratio': 'loss_ratio'
    }

    def __init__(self, id=None, vif_peer_id=None, project_id=None, domain_id=None, start_time=None, end_time=None, status=None, loss_ratio=None):
        r"""VifPeerDetection

        The model defined in huaweicloud sdk

        :param id: 虚拟接口对等体连通性探测实例uuid
        :type id: str
        :param vif_peer_id: 虚拟接口对等体实例uuid
        :type vif_peer_id: str
        :param project_id: 租户id
        :type project_id: str
        :param domain_id: 账号id
        :type domain_id: str
        :param start_time: 探测开始时间
        :type start_time: str
        :param end_time: 探测结束时间
        :type end_time: str
        :param status: 探测状态，取值范围： - processing: 探测处理中 - complete: 探测完成 - error: 探测异常退出
        :type status: str
        :param loss_ratio: 丢包率
        :type loss_ratio: int
        """
        
        

        self._id = None
        self._vif_peer_id = None
        self._project_id = None
        self._domain_id = None
        self._start_time = None
        self._end_time = None
        self._status = None
        self._loss_ratio = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if vif_peer_id is not None:
            self.vif_peer_id = vif_peer_id
        if project_id is not None:
            self.project_id = project_id
        if domain_id is not None:
            self.domain_id = domain_id
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if status is not None:
            self.status = status
        if loss_ratio is not None:
            self.loss_ratio = loss_ratio

    @property
    def id(self):
        r"""Gets the id of this VifPeerDetection.

        虚拟接口对等体连通性探测实例uuid

        :return: The id of this VifPeerDetection.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this VifPeerDetection.

        虚拟接口对等体连通性探测实例uuid

        :param id: The id of this VifPeerDetection.
        :type id: str
        """
        self._id = id

    @property
    def vif_peer_id(self):
        r"""Gets the vif_peer_id of this VifPeerDetection.

        虚拟接口对等体实例uuid

        :return: The vif_peer_id of this VifPeerDetection.
        :rtype: str
        """
        return self._vif_peer_id

    @vif_peer_id.setter
    def vif_peer_id(self, vif_peer_id):
        r"""Sets the vif_peer_id of this VifPeerDetection.

        虚拟接口对等体实例uuid

        :param vif_peer_id: The vif_peer_id of this VifPeerDetection.
        :type vif_peer_id: str
        """
        self._vif_peer_id = vif_peer_id

    @property
    def project_id(self):
        r"""Gets the project_id of this VifPeerDetection.

        租户id

        :return: The project_id of this VifPeerDetection.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this VifPeerDetection.

        租户id

        :param project_id: The project_id of this VifPeerDetection.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def domain_id(self):
        r"""Gets the domain_id of this VifPeerDetection.

        账号id

        :return: The domain_id of this VifPeerDetection.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this VifPeerDetection.

        账号id

        :param domain_id: The domain_id of this VifPeerDetection.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def start_time(self):
        r"""Gets the start_time of this VifPeerDetection.

        探测开始时间

        :return: The start_time of this VifPeerDetection.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this VifPeerDetection.

        探测开始时间

        :param start_time: The start_time of this VifPeerDetection.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this VifPeerDetection.

        探测结束时间

        :return: The end_time of this VifPeerDetection.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this VifPeerDetection.

        探测结束时间

        :param end_time: The end_time of this VifPeerDetection.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def status(self):
        r"""Gets the status of this VifPeerDetection.

        探测状态，取值范围： - processing: 探测处理中 - complete: 探测完成 - error: 探测异常退出

        :return: The status of this VifPeerDetection.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this VifPeerDetection.

        探测状态，取值范围： - processing: 探测处理中 - complete: 探测完成 - error: 探测异常退出

        :param status: The status of this VifPeerDetection.
        :type status: str
        """
        self._status = status

    @property
    def loss_ratio(self):
        r"""Gets the loss_ratio of this VifPeerDetection.

        丢包率

        :return: The loss_ratio of this VifPeerDetection.
        :rtype: int
        """
        return self._loss_ratio

    @loss_ratio.setter
    def loss_ratio(self, loss_ratio):
        r"""Sets the loss_ratio of this VifPeerDetection.

        丢包率

        :param loss_ratio: The loss_ratio of this VifPeerDetection.
        :type loss_ratio: int
        """
        self._loss_ratio = loss_ratio

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
        if not isinstance(other, VifPeerDetection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
