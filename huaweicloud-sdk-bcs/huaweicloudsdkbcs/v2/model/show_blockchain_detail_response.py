# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowBlockchainDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'basic_info': 'BasicInfo',
        'channels': 'list[ChannelInfo]',
        'peer_info': 'list[PeerInfo]',
        'light_peer_info': 'list[PeerInfo]',
        'orderer_info': 'PeerInfo',
        'couch_db_info': 'CouchDBInfo',
        'dms_kafka_info': 'DmsKafkaInfo',
        'ief_info': 'IefInfo',
        'sfs_info': 'SfsInfo',
        'agent_info': 'PeerInfo',
        'restapi_info': 'PeerInfo',
        'evs_pvc_info': 'dict(str, dict(str, str))',
        'tc3_taskserver_info': 'PeerInfo',
        'obs_bucket_info': 'OBSInfo'
    }

    attribute_map = {
        'basic_info': 'basic_info',
        'channels': 'channels',
        'peer_info': 'peer_info',
        'light_peer_info': 'light_peer_info',
        'orderer_info': 'orderer_info',
        'couch_db_info': 'couch_db_info',
        'dms_kafka_info': 'dms_kafka_info',
        'ief_info': 'ief_info',
        'sfs_info': 'sfs_info',
        'agent_info': 'agent_info',
        'restapi_info': 'restapi_info',
        'evs_pvc_info': 'evs_pvc_info',
        'tc3_taskserver_info': 'tc3_taskserver_info',
        'obs_bucket_info': 'obs_bucket_info'
    }

    def __init__(self, basic_info=None, channels=None, peer_info=None, light_peer_info=None, orderer_info=None, couch_db_info=None, dms_kafka_info=None, ief_info=None, sfs_info=None, agent_info=None, restapi_info=None, evs_pvc_info=None, tc3_taskserver_info=None, obs_bucket_info=None):
        """ShowBlockchainDetailResponse

        The model defined in huaweicloud sdk

        :param basic_info: 
        :type basic_info: :class:`huaweicloudsdkbcs.v2.BasicInfo`
        :param channels: 通道信息
        :type channels: list[:class:`huaweicloudsdkbcs.v2.ChannelInfo`]
        :param peer_info: peer组织信息
        :type peer_info: list[:class:`huaweicloudsdkbcs.v2.PeerInfo`]
        :param light_peer_info: light_peer组织信息
        :type light_peer_info: list[:class:`huaweicloudsdkbcs.v2.PeerInfo`]
        :param orderer_info: 
        :type orderer_info: :class:`huaweicloudsdkbcs.v2.PeerInfo`
        :param couch_db_info: 
        :type couch_db_info: :class:`huaweicloudsdkbcs.v2.CouchDBInfo`
        :param dms_kafka_info: 
        :type dms_kafka_info: :class:`huaweicloudsdkbcs.v2.DmsKafkaInfo`
        :param ief_info: 
        :type ief_info: :class:`huaweicloudsdkbcs.v2.IefInfo`
        :param sfs_info: 
        :type sfs_info: :class:`huaweicloudsdkbcs.v2.SfsInfo`
        :param agent_info: 
        :type agent_info: :class:`huaweicloudsdkbcs.v2.PeerInfo`
        :param restapi_info: 
        :type restapi_info: :class:`huaweicloudsdkbcs.v2.PeerInfo`
        :param evs_pvc_info: 云硬盘存储卷信息
        :type evs_pvc_info: dict(str, dict(str, str))
        :param tc3_taskserver_info: 
        :type tc3_taskserver_info: :class:`huaweicloudsdkbcs.v2.PeerInfo`
        :param obs_bucket_info: 
        :type obs_bucket_info: :class:`huaweicloudsdkbcs.v2.OBSInfo`
        """
        
        super(ShowBlockchainDetailResponse, self).__init__()

        self._basic_info = None
        self._channels = None
        self._peer_info = None
        self._light_peer_info = None
        self._orderer_info = None
        self._couch_db_info = None
        self._dms_kafka_info = None
        self._ief_info = None
        self._sfs_info = None
        self._agent_info = None
        self._restapi_info = None
        self._evs_pvc_info = None
        self._tc3_taskserver_info = None
        self._obs_bucket_info = None
        self.discriminator = None

        if basic_info is not None:
            self.basic_info = basic_info
        if channels is not None:
            self.channels = channels
        if peer_info is not None:
            self.peer_info = peer_info
        if light_peer_info is not None:
            self.light_peer_info = light_peer_info
        if orderer_info is not None:
            self.orderer_info = orderer_info
        if couch_db_info is not None:
            self.couch_db_info = couch_db_info
        if dms_kafka_info is not None:
            self.dms_kafka_info = dms_kafka_info
        if ief_info is not None:
            self.ief_info = ief_info
        if sfs_info is not None:
            self.sfs_info = sfs_info
        if agent_info is not None:
            self.agent_info = agent_info
        if restapi_info is not None:
            self.restapi_info = restapi_info
        if evs_pvc_info is not None:
            self.evs_pvc_info = evs_pvc_info
        if tc3_taskserver_info is not None:
            self.tc3_taskserver_info = tc3_taskserver_info
        if obs_bucket_info is not None:
            self.obs_bucket_info = obs_bucket_info

    @property
    def basic_info(self):
        """Gets the basic_info of this ShowBlockchainDetailResponse.

        :return: The basic_info of this ShowBlockchainDetailResponse.
        :rtype: :class:`huaweicloudsdkbcs.v2.BasicInfo`
        """
        return self._basic_info

    @basic_info.setter
    def basic_info(self, basic_info):
        """Sets the basic_info of this ShowBlockchainDetailResponse.

        :param basic_info: The basic_info of this ShowBlockchainDetailResponse.
        :type basic_info: :class:`huaweicloudsdkbcs.v2.BasicInfo`
        """
        self._basic_info = basic_info

    @property
    def channels(self):
        """Gets the channels of this ShowBlockchainDetailResponse.

        通道信息

        :return: The channels of this ShowBlockchainDetailResponse.
        :rtype: list[:class:`huaweicloudsdkbcs.v2.ChannelInfo`]
        """
        return self._channels

    @channels.setter
    def channels(self, channels):
        """Sets the channels of this ShowBlockchainDetailResponse.

        通道信息

        :param channels: The channels of this ShowBlockchainDetailResponse.
        :type channels: list[:class:`huaweicloudsdkbcs.v2.ChannelInfo`]
        """
        self._channels = channels

    @property
    def peer_info(self):
        """Gets the peer_info of this ShowBlockchainDetailResponse.

        peer组织信息

        :return: The peer_info of this ShowBlockchainDetailResponse.
        :rtype: list[:class:`huaweicloudsdkbcs.v2.PeerInfo`]
        """
        return self._peer_info

    @peer_info.setter
    def peer_info(self, peer_info):
        """Sets the peer_info of this ShowBlockchainDetailResponse.

        peer组织信息

        :param peer_info: The peer_info of this ShowBlockchainDetailResponse.
        :type peer_info: list[:class:`huaweicloudsdkbcs.v2.PeerInfo`]
        """
        self._peer_info = peer_info

    @property
    def light_peer_info(self):
        """Gets the light_peer_info of this ShowBlockchainDetailResponse.

        light_peer组织信息

        :return: The light_peer_info of this ShowBlockchainDetailResponse.
        :rtype: list[:class:`huaweicloudsdkbcs.v2.PeerInfo`]
        """
        return self._light_peer_info

    @light_peer_info.setter
    def light_peer_info(self, light_peer_info):
        """Sets the light_peer_info of this ShowBlockchainDetailResponse.

        light_peer组织信息

        :param light_peer_info: The light_peer_info of this ShowBlockchainDetailResponse.
        :type light_peer_info: list[:class:`huaweicloudsdkbcs.v2.PeerInfo`]
        """
        self._light_peer_info = light_peer_info

    @property
    def orderer_info(self):
        """Gets the orderer_info of this ShowBlockchainDetailResponse.

        :return: The orderer_info of this ShowBlockchainDetailResponse.
        :rtype: :class:`huaweicloudsdkbcs.v2.PeerInfo`
        """
        return self._orderer_info

    @orderer_info.setter
    def orderer_info(self, orderer_info):
        """Sets the orderer_info of this ShowBlockchainDetailResponse.

        :param orderer_info: The orderer_info of this ShowBlockchainDetailResponse.
        :type orderer_info: :class:`huaweicloudsdkbcs.v2.PeerInfo`
        """
        self._orderer_info = orderer_info

    @property
    def couch_db_info(self):
        """Gets the couch_db_info of this ShowBlockchainDetailResponse.

        :return: The couch_db_info of this ShowBlockchainDetailResponse.
        :rtype: :class:`huaweicloudsdkbcs.v2.CouchDBInfo`
        """
        return self._couch_db_info

    @couch_db_info.setter
    def couch_db_info(self, couch_db_info):
        """Sets the couch_db_info of this ShowBlockchainDetailResponse.

        :param couch_db_info: The couch_db_info of this ShowBlockchainDetailResponse.
        :type couch_db_info: :class:`huaweicloudsdkbcs.v2.CouchDBInfo`
        """
        self._couch_db_info = couch_db_info

    @property
    def dms_kafka_info(self):
        """Gets the dms_kafka_info of this ShowBlockchainDetailResponse.

        :return: The dms_kafka_info of this ShowBlockchainDetailResponse.
        :rtype: :class:`huaweicloudsdkbcs.v2.DmsKafkaInfo`
        """
        return self._dms_kafka_info

    @dms_kafka_info.setter
    def dms_kafka_info(self, dms_kafka_info):
        """Sets the dms_kafka_info of this ShowBlockchainDetailResponse.

        :param dms_kafka_info: The dms_kafka_info of this ShowBlockchainDetailResponse.
        :type dms_kafka_info: :class:`huaweicloudsdkbcs.v2.DmsKafkaInfo`
        """
        self._dms_kafka_info = dms_kafka_info

    @property
    def ief_info(self):
        """Gets the ief_info of this ShowBlockchainDetailResponse.

        :return: The ief_info of this ShowBlockchainDetailResponse.
        :rtype: :class:`huaweicloudsdkbcs.v2.IefInfo`
        """
        return self._ief_info

    @ief_info.setter
    def ief_info(self, ief_info):
        """Sets the ief_info of this ShowBlockchainDetailResponse.

        :param ief_info: The ief_info of this ShowBlockchainDetailResponse.
        :type ief_info: :class:`huaweicloudsdkbcs.v2.IefInfo`
        """
        self._ief_info = ief_info

    @property
    def sfs_info(self):
        """Gets the sfs_info of this ShowBlockchainDetailResponse.

        :return: The sfs_info of this ShowBlockchainDetailResponse.
        :rtype: :class:`huaweicloudsdkbcs.v2.SfsInfo`
        """
        return self._sfs_info

    @sfs_info.setter
    def sfs_info(self, sfs_info):
        """Sets the sfs_info of this ShowBlockchainDetailResponse.

        :param sfs_info: The sfs_info of this ShowBlockchainDetailResponse.
        :type sfs_info: :class:`huaweicloudsdkbcs.v2.SfsInfo`
        """
        self._sfs_info = sfs_info

    @property
    def agent_info(self):
        """Gets the agent_info of this ShowBlockchainDetailResponse.

        :return: The agent_info of this ShowBlockchainDetailResponse.
        :rtype: :class:`huaweicloudsdkbcs.v2.PeerInfo`
        """
        return self._agent_info

    @agent_info.setter
    def agent_info(self, agent_info):
        """Sets the agent_info of this ShowBlockchainDetailResponse.

        :param agent_info: The agent_info of this ShowBlockchainDetailResponse.
        :type agent_info: :class:`huaweicloudsdkbcs.v2.PeerInfo`
        """
        self._agent_info = agent_info

    @property
    def restapi_info(self):
        """Gets the restapi_info of this ShowBlockchainDetailResponse.

        :return: The restapi_info of this ShowBlockchainDetailResponse.
        :rtype: :class:`huaweicloudsdkbcs.v2.PeerInfo`
        """
        return self._restapi_info

    @restapi_info.setter
    def restapi_info(self, restapi_info):
        """Sets the restapi_info of this ShowBlockchainDetailResponse.

        :param restapi_info: The restapi_info of this ShowBlockchainDetailResponse.
        :type restapi_info: :class:`huaweicloudsdkbcs.v2.PeerInfo`
        """
        self._restapi_info = restapi_info

    @property
    def evs_pvc_info(self):
        """Gets the evs_pvc_info of this ShowBlockchainDetailResponse.

        云硬盘存储卷信息

        :return: The evs_pvc_info of this ShowBlockchainDetailResponse.
        :rtype: dict(str, dict(str, str))
        """
        return self._evs_pvc_info

    @evs_pvc_info.setter
    def evs_pvc_info(self, evs_pvc_info):
        """Sets the evs_pvc_info of this ShowBlockchainDetailResponse.

        云硬盘存储卷信息

        :param evs_pvc_info: The evs_pvc_info of this ShowBlockchainDetailResponse.
        :type evs_pvc_info: dict(str, dict(str, str))
        """
        self._evs_pvc_info = evs_pvc_info

    @property
    def tc3_taskserver_info(self):
        """Gets the tc3_taskserver_info of this ShowBlockchainDetailResponse.

        :return: The tc3_taskserver_info of this ShowBlockchainDetailResponse.
        :rtype: :class:`huaweicloudsdkbcs.v2.PeerInfo`
        """
        return self._tc3_taskserver_info

    @tc3_taskserver_info.setter
    def tc3_taskserver_info(self, tc3_taskserver_info):
        """Sets the tc3_taskserver_info of this ShowBlockchainDetailResponse.

        :param tc3_taskserver_info: The tc3_taskserver_info of this ShowBlockchainDetailResponse.
        :type tc3_taskserver_info: :class:`huaweicloudsdkbcs.v2.PeerInfo`
        """
        self._tc3_taskserver_info = tc3_taskserver_info

    @property
    def obs_bucket_info(self):
        """Gets the obs_bucket_info of this ShowBlockchainDetailResponse.

        :return: The obs_bucket_info of this ShowBlockchainDetailResponse.
        :rtype: :class:`huaweicloudsdkbcs.v2.OBSInfo`
        """
        return self._obs_bucket_info

    @obs_bucket_info.setter
    def obs_bucket_info(self, obs_bucket_info):
        """Sets the obs_bucket_info of this ShowBlockchainDetailResponse.

        :param obs_bucket_info: The obs_bucket_info of this ShowBlockchainDetailResponse.
        :type obs_bucket_info: :class:`huaweicloudsdkbcs.v2.OBSInfo`
        """
        self._obs_bucket_info = obs_bucket_info

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
        if not isinstance(other, ShowBlockchainDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
